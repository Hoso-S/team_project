proc_name = 'guni_conf_staging' # The proc name must be set to the same value as the filename of gunicorn config.
pythonpath = 'sql_app'
wsgi_app = 'sql_app.main:app'
workers = 2
worker_class = 'uvicorn.workers.UvicornWorker'
bind = 'localhost:8080'
raw_env = ['MODE=STAGING']
daemon = True
pidfile = './logs/staging.pid'
errorlog = './logs/staging_error_log.txt'
accesslog = './logs/staging_access_log.txt'
loglevel = 'info'
capture_output = True
