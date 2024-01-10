proc_name = 'guni_conf_prod' # The proc name must be set to the same value as the filename of gunicorn config.
pythonpath = 'sql_app'
wsgi_app = 'sql_app.main:app'
workers = 2
worker_class = 'uvicorn.workers.UvicornWorker'
bind = '0.0.0.0:8080'
raw_env = ['MODE=PROD']
daemon = True
pidfile = './logs/prod.pid'
errorlog = './logs/prod_error_log.txt'
accesslog = './logs/prod_access_log.txt'
loglevel = 'info'
capture_output = True
