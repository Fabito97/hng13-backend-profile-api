from datetime import datetime
from fastapi import FastAPI
from utils import get_fact
import dotenv
import os

dotenv.load_dotenv()

app = FastAPI()


EMAIL = os.getenv("EMAIL")
NAME  = os.getenv("NAME")
STACK = os.getenv("STACK")


@app.get("/me")
async def get_profile():
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

