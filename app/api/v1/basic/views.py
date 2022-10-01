from typing import Any

from fastapi import APIRouter

from app import schemas
from app.core.config import settings

router = APIRouter()


@router.get(
    "/",
    tags=["basic"],
    response_model=schemas.basic.BasicMessage,
)
async def basic() -> Any:
    msg = schemas.basic.BasicMessage(
        msg=f"Welcome to `{settings.SERVER_NAME}`",
    )
    return msg
