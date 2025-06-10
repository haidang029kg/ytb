import os
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
	# general
	ROOT_DIR: Path = Field(default=Path.cwd(), description="Project root directory")

	# logging
	LOG_DIR: Path = Field(
		default_factory=lambda: Path.cwd() / "logs", description="Directory for log files"
	)
	LOG_BACKUP_COUNT: int = Field(default=30, description="Number of log backups to keep")

	# authentication
	SECRET_KEY: str = Field(default="123abc123")
	ALGORITHM: str = Field(default="HS256")
	ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30)
	ACCESS_TOKEN_MAX_LIFETIME_DAYS: int = Field(default=45)
	REFRESH_TOKEN_EXPIRE_DAYS: int = Field(default=7)

	# database
	DB_URL: str = Field(default="sqlite:///db.sqlite")
	DB_URL_ASYNC: str = Field(default="sqlite+aiosqlite:///db.sqlite")

	class Config:
		# load defaults from a .env file in project root, if present
		env_file = ".env"
		case_sensitive = True


# create a single, ready-to-use settings instance
settings = Settings()
