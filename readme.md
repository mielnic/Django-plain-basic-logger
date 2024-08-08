## Logger app for Django ##

Very simple logging app for Django. It adds asection to the Django Admin, and displays the last n files of a logfile stored under `log`folder in the root directory, in reverse order.

Configs for the `settings.py` file:

LOGDIR = (os.path.join(BASE_DIR, 'log'))
LOGFILE = f'{LOGDIR}/logfile.log'
LOG_LINES = 200

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'logfile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOGFILE,
            'formatter': 'simple',
        },
    },
    'loggers': {
        'logger': {
            'handlers': ['logfile'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

In each file:

`import logging`
`logger = logging.getLogger('logfile')`