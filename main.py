from datetime import datetime
from fastapi import HTTPException
from fastapi import FastAPI
from pydantic import BaseModel
from utils import get_fact

app = FastAPI()


email = "fabbenco97@gmail.com"
name  = "Fabian Muoghalu"
stack = "C#, Python, NodeJs"


@app.get("/me")
async def get_profile():
    """
    Returns user info and a cat fact or fallback joke.
    """
    fact = await get_fact()

    return {
      "status": "success",
      "user": {
        "email": email,
        "name": name,
        "stack": stack
      },
      "timestamp": datetime.utcnow(),
      "fact": fact
    }

