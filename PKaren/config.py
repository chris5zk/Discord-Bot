import logging
import os
import time

from logging.config import dictConfig
from dotenv import load_dotenv


load_dotenv()

DISCORD_API_SECRET = os.getenv('TOKEN')

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)-10s] %(name)-12s: %(message)s",
            "datefmt": '%Y-%m-%d %H:%M:%S'
        },
        "chat": {
            "format": '[%(asctime)s %(name)s][%(levelname)s] %(message)s',
            "datefmt": '%Y-%m-%d %H:%M:%S'
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "filename": f"logs/{time.strftime('%Y-%m-%d')}.log",
            "formatter": "default",
            "maxBytes": 128 * 1024 * 1024,
            "backupCount": 24
        }
    },
    "loggers": {
        "discord": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        }
    },
    "disable_existing_loggers": False
}

dictConfig(LOGGING_CONFIG)
