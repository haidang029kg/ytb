import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from src import settings

logger = logging.getLogger()
payment_logger = logging.getLogger("payment")

# log formatter
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

os.makedirs(os.path.join(settings.LOG_DIR), exist_ok=True)
os.makedirs(os.path.join(settings.LOG_DIR, "payment"), exist_ok=True)

# create handlers
stream_handler = logging.StreamHandler(sys.stdout)
file_rotate_handler = TimedRotatingFileHandler(
	filename=os.path.join(settings.LOG_DIR, "app.log"),
	when="midnight",
	interval=1,
	backupCount=settings.LOG_BACKUP_COUNT,
)
payment_file_rotate_handler = TimedRotatingFileHandler(
	filename=os.path.join(settings.LOG_DIR, "payment", "payment.log"),
	when="midnight",
	interval=1,
	backupCount=settings.LOG_BACKUP_COUNT,
)

# set formatter
stream_handler.setFormatter(formatter)
file_rotate_handler.setFormatter(formatter)
payment_file_rotate_handler.setFormatter(formatter)


# add handler to the log
logger.handlers = [
	stream_handler,
	file_rotate_handler,
]

payment_logger.handlers = [
	payment_file_rotate_handler,
]

# set log level
logger.setLevel(logging.INFO)
payment_logger.setLevel(logging.INFO)
