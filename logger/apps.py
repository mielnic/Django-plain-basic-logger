# logger/apps.py
from django.apps import AppConfig
import logging.config
from django.conf import settings

class LoggerConfig(AppConfig):
    name = 'logger'

    def ready(self):
        from .utils import DatabaseLogHandler
        LOGGING = {
            'version': 1,
            'disable_existing_loggers': True,
            'handlers': {
                'logfile': {
                    'level': 'INFO',
                    'class': 'logging.FileHandler',
                    'filename': settings.LOGFILE, 
                    'formatter': 'simple',
                },
                'db': {
                    'level': 'INFO',
                    'class': 'logger.utils.DatabaseLogHandler',
                },
            },
            'loggers': {
                '': {
                    'handlers': ['logfile', 'db'],
                    'level': 'INFO',
                    'propagate': True,
                },
            },
            'formatters': {
                'simple': {
                    'format': '{asctime} {levelname} {message}',
                    'style': '{',
                },
            },
        }

        logging.config.dictConfig(LOGGING)
