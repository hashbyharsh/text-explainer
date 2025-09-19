from fastapi import Depends, FastAPI, HTTPException
from langchain_openai import ChatOpenAI
import redis
import hmac
import hashlib
from src.endpoints.explain import TextRequest, explain_text, verify_token
from fastapi.middleware.cors import CORSMiddleware
from src.config.config import config

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Redis client
redis_client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

# Initialize Groq client
llm = ChatOpenAI(model="gpt-4o-mini", api_key=config.OPENAI_API_KEY)

# Include endpoints
@app.get("/get-token")
async def get_token():
    try:
        token = hmac.new(
            config.SECRET_KEY.encode('utf-8'),
            config.EXPECTED_MESSAGE.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        return {"token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate token: {str(e)}")
    
@app.post("/explain")
async def explain_endpoint(request: TextRequest, token: str = Depends(verify_token)):
    return await explain_text(redis_client, llm, request, token)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)