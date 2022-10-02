from functools import lru_cache
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, MongoDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    BACKEND_CORS_ORIGINS: Union[List[AnyHttpUrl], AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
        cls,
        v: Union[str, List[str]],
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str
    MONGODB_DATABASE: str
    MONGODB_INITIAL_PRIMARY_HOST: str
    MONGODB_PORT_NUMBER: str
    DB_QUERY: Optional[str]

    MONGODB_URL: Optional[str]

    @validator("MONGODB_URL", pre=True)
    def assemble_db_connection(
        cls,
        v: Optional[str],
        values: Dict[str, Any],
    ) -> str:
        if isinstance(v, str):
            return v
        return MongoDsn.build(
            scheme="mongodb",
            user=values.get("MONGODB_USERNAME"),
            password=values.get("MONGODB_PASSWORD"),
            host=values.get("MONGODB_INITIAL_PRIMARY_HOST"),
            port=values.get("MONGODB_PORT_NUMBER"),
            path=f"/{values.get('MONGODB_DATABASE') or ''}",
            query=values.get("DB_QUERY"),
        )

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache(maxsize=128)
def get_settings():
    return Settings()


settings = get_settings()
