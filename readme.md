## Logger app for Django ##

Very simple logging app for Django. It adds asection to the Django Admin, and displays the last n files of a logfile stored under `log`folder in the root directory, in reverse order.

Configs for the `settings.py` file:

LOGDIR = (os.path.join(BASE_DIR, 'log'))
LOGFILE = f'{LOGDIR}/logfile.log'
LOG_RETENTION_DAYS = 30

In each file:

`import logging`
`logger = logging.getLogger('logfile')`