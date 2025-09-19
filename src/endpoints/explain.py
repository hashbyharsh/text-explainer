from fastapi import HTTPException, Depends, Header
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from redis import Redis
from typing import Optional
from src.config.config import config
from src.prompts.prompts import CONTEXT_PROMPT_NORMAL, CONTEXT_PROMPT_SIMPLIFY
from src.utils.helpers import get_text_hash, is_gibberish, store_search_text
from src.utils.enum import VehicleType
import time
import hmac
import hashlib

class TextRequest(BaseModel):
    selected_text: str
    type: VehicleType
    context: Optional[str] = None 
    locale: str = "en"
    simplify: bool = False

def verify_token(authorization: str = Header(...)):
    """Verify the token in the Authorization header."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    token = authorization.split("Bearer ")[1]
    expected_signature = hmac.new(
        config.SECRET_KEY.encode(), config.EXPECTED_MESSAGE.encode(), hashlib.sha256
    ).hexdigest()
    if not hmac.compare_digest(expected_signature, token):
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

def check_rate_limit(redis_client: Redis, token: str):
    """Check and update rate limit for the given token."""
    rate_key = f"rate:{token}"
    current_time = int(time.time())
    window_start = current_time - config.RATE_LIMIT_WINDOW

    pipe = redis_client.pipeline()
    pipe.zremrangebyscore(rate_key, 0, window_start)
    pipe.zcard(rate_key)
    pipe.expire(rate_key, config.RATE_LIMIT_WINDOW)
    _, count, _ = pipe.execute()

    print(f"Rate key: {rate_key}, Count: {count}, Window: {config.RATE_LIMIT_WINDOW}")

    if count >= config.RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    redis_client.zadd(rate_key, {str(current_time): current_time})

async def explain_text(redis_client: Redis, llm: ChatOpenAI, request: TextRequest, token: str = Depends(verify_token)):
    try:
        selected_text = request.selected_text.strip()
        if not selected_text:
            raise HTTPException(status_code=400, detail="Missing selected_text")
        
        # Validate selected_text length
        if len(selected_text) > 200:
            raise HTTPException(status_code=400, detail="Selected text exceeds 200 character limit")

        # Always use static context based on type
        context = config.STATIC_CONTEXTS.get(request.type.value)
        if not context:
            raise HTTPException(status_code=400, detail=f"No context defined for type: {request.type.value}")

        locale = request.locale.strip() if request.locale else "en"
        simplify = request.simplify

        if locale not in config.VALID_LOCALES:
            raise HTTPException(status_code=400, detail="Invalid locale. Choose en, hi, te, ta, pb, or mr.")

        check_rate_limit(redis_client, token)

        if is_gibberish(selected_text):
            return {"explanation": config.GIBBERISH_MESSAGE.get(locale, config.GIBBERISH_MESSAGE["en"]).format(selected_text=selected_text)}

        cache_key = get_text_hash(selected_text, context, locale, simplify)
        cached_explanation = redis_client.get(cache_key)
        if cached_explanation:
            store_search_text(redis_client, selected_text, cache_key, config.CACHE_TTL)
            return {"explanation": cached_explanation}

        language = config.LANGUAGE_MAP.get(locale, "English")

        # Always use context-based prompt since static context is guaranteed
        if simplify:
            prompt = CONTEXT_PROMPT_SIMPLIFY.format(selected_text=selected_text, context=context, language=language)
        else:
            prompt = CONTEXT_PROMPT_NORMAL.format(selected_text=selected_text, context=context, language=language)
        response = llm.invoke(prompt)
        explanation = response.content.strip()

        redis_client.setex(cache_key, config.CACHE_TTL, explanation)
        store_search_text(redis_client, selected_text, cache_key, config.CACHE_TTL)

        return {"explanation": explanation}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate explanation: {str(e)}")