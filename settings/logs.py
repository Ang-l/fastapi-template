# logs.py

import logging.config

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "user_file_handler": {
            "class": "logging.FileHandler",
            "filename": "logs/user.log",
            "formatter": "default",
            "level": "INFO",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
    },
    "loggers": {
        "user_logger": {
            "level": "INFO",
            "handlers": ["console", "user_file_handler"],
            "propagate": False,
        },
    },
}

# 应用日志配置
logging.config.dictConfig(LOG_CONFIG)