import os
from pathlib import Path

# general
ROOT_DIR = Path.cwd()

# logging
LOG_DIR = os.path.join(ROOT_DIR, "logs")
LOG_BACKUP_COUNT = 30

# authentication
SECRET_KEY = "123abc123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ACCESS_TOKEN_MAX_LIFE_TIME_DAYS = 45
REFRESH_TOKEN_EXPIRE_DAYS = 7

# database
DB_URL = "sqlite:///db.sqlite"
DB_URL_ASYNC = "sqlite+aiosqlite:///db.sqlite"
