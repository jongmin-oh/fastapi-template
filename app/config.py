from pathlib import Path
from typing import Optional
from pydantic import BaseSettings, BaseModel


class Paths(BaseModel):
    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    LOGS_DIR: Path = BASE_DIR.joinpath("logs")


class Config(BaseSettings):

    """Deploy configurations."""

    app_path: Paths = Paths()

    HOST: Optional[str] = None
    PORT: Optional[int] = None
    LOG_LEVEL: Optional[str] = None

    class Config:
        env_file: str = ".env"


settings = Config()
