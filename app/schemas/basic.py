from pydantic import BaseModel


__all__ = (
    "BasicMessage",
)


class BasicMessage(BaseModel):
    msg: str

    class Config:
        schema_extra = {
            "example": {
                "msg": "Hello world",
            }
        }
