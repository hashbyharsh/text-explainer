from fastapi import Depends, FastAPI
from langchain_groq import ChatGroq
import redis
from src.endpoints.explain import TextRequest, explain_text
from src.config.config import config

# Initialize FastAPI app
app = FastAPI()

# Initialize Redis client
redis_client = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)

# Initialize Groq client
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=config.GROQ_API_KEY)

# Include endpoints
@app.post("/explain")
async def explain_endpoint(request: TextRequest):
    return await explain_text(redis_client, llm, request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)