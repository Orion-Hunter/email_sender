from typing import Optional
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    SMTP_EMAIL_SENDER: str = Field(
        env="SMTP_EMAIL_SENDER", default="developer@gmail.com"
    )
    SMTP_HOST: str = Field(env="SMTP_HOST")
    SMTP_PORT: int = Field(env="SMTP_PORT", default=587)
    SMTP_USERNAME: Optional[str] = Field(env="SMTP_USERNAME")
    SMTP_PASSWORD: Optional[str] = Field(env="SMTP_PASSWORD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
