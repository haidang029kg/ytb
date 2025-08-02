import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from src.core.ctx_vars import request_id_ctx_var
from src.core.settings import settings

# log formatter
formatter = logging.Formatter(
	fmt="%(asctime)s - %(levelname)s - %(request_id)s - logger=%(name)s - %(module)s:%(lineno)d - %(message)s"
)


# Custom logging filter to add UUID from context
class RequestIdFilter(logging.Filter):
	def filter(self, record):
		record.request_id = request_id_ctx_var.get()
		return True


logger = logging.getLogger()
payment_logger = logging.getLogger("payment")

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

# add filter
request_id_filter = RequestIdFilter()

stream_handler.addFilter(request_id_filter)
file_rotate_handler.addFilter(request_id_filter)
payment_file_rotate_handler.addFilter(request_id_filter)

# add handler to the log
if not logger.handlers:
	logger.addHandler(stream_handler)
	logger.addHandler(file_rotate_handler)

if not payment_logger.handlers:
	payment_logger.addHandler(payment_file_rotate_handler)

# set log level
logger.setLevel(logging.INFO)
payment_logger.setLevel(logging.INFO)
