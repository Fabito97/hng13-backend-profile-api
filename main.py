from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from utils import get_fact

import dotenv
import os

dotenv.load_dotenv()

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
async def custom_rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"status": "error", "message": "Too many requests. Please try again later."}
    )


EMAIL = os.getenv("EMAIL")
NAME  = os.getenv("NAME")
STACK = os.getenv("STACK")


@app.get("/me")
@limiter.limit("5/minute")  # ⏱️ Allow 5 requests per minute per IP
async def get_profile(request: Request):
    """
    Returns user info and a cat fact or fallback joke.
    """
    fact = await get_fact()

    return {
      "status": "success",
      "user": {
        "email": EMAIL,
        "name": NAME,
        "stack": STACK
      },
      "timestamp": datetime.utcnow(),
      "fact": fact
    }

