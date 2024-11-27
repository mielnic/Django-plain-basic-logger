## Logger app for Django ##

Very simple logging app for Django. Logs to database and to a file, with different loglevels.

Database model is added to the Django Admin, and suport standadar and exclsion search by preceding the searc hterm with !.

Cron in crons.py can be used with django-cron to remove old logs. A management command is avaiable with the same purpose.

Configs for the `settings.py` file:

LOGDIR = (os.path.join(BASE_DIR, 'log'))
LOGFILE = f'{LOGDIR}/logfile.log'
LOG_RETENTION_DAYS = 30
FILE_LOGLEVEL = 'DEBUG'
DB_LOGLEVEL= 'INFO'

In each file:

`import logging`
`logger = logging.getLogger('logfile')`