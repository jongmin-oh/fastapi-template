from fastapi import Header, HTTPException
from app.config import settings


async def get_token_header(x_token: str = Header(...)):
    if x_token != settings.ACCESS_TOKEN:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
