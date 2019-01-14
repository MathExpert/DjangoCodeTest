import os

# A base to use with setproctitle for process naming.
# http://docs.gunicorn.org/en/stable/settings.html#proc-name
_proc_name = os.environ.get('GUNICORN_PROC_NAME', 'cloud-code-test')
if _proc_name:
    proc_name = _proc_name

# The socket to bind.
# Comma separated string.
# http://docs.gunicorn.org/en/stable/settings.html#bind
_bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8000')
if _bind:
    bind = _bind.split(',')


# Worker config

# The type of workers to use.
# http://docs.gunicorn.org/en/stable/settings.html#worker-class
_worker_class = os.environ.get('GUNICORN_WORKER_CLASS', 'sync')
if _worker_class:
    worker_class = _worker_class

# The number of worker processes for handling requests.
# http://docs.gunicorn.org/en/stable/settings.html#workers
_workers = os.environ.get('GUNICORN_WORKERS', 3)
if _workers:
    workers = int(_workers)

# The maximum number of requests a worker will process before restarting
# http://docs.gunicorn.org/en/stable/settings.html#max-requests
_max_requests = os.environ.get('GUNICORN_MAX_REQUESTS', 2000)
if _max_requests:
    max_requests = int(_max_requests)

# The maximum jitter to add to the max_requests setting
# http://docs.gunicorn.org/en/stable/settings.html#max-requests-jitter
_max_requests_jitter = os.environ.get('GUNICORN_MAX_REQUESTS_JITTER', 37)
if _max_requests_jitter:
    max_requests_jitter = int(_max_requests_jitter)

# Workers silent for more than this many seconds are killed and restarted
# http://docs.gunicorn.org/en/stable/settings.html#timeout
_timeout = os.environ.get('GUNICORN_TIMEOUT', 30)
if _timeout:
    timeout = int(_timeout)

# Timeout for graceful workers restart.
# http://docs.gunicorn.org/en/stable/settings.html#graceful-timeout
_graceful_timeout = os.environ.get('GUNICORN_GRACEFUL_TIMEOUT', 30)
if _graceful_timeout:
    graceful_timeout = int(_graceful_timeout)


# Logging config:

# The Access log file to write to.
# http://docs.gunicorn.org/en/stable/settings.html#accesslog
_accesslog = os.environ.get('GUNICORN_ACCESSLOG', '-')
if _accesslog:
    accesslog = _accesslog

# The access log format.
# http://docs.gunicorn.org/en/stable/settings.html#access-log-format
_access_log_format = os.environ.get(
    'GUNICORN_ACCESS_LOG_FORMAT',
    'ACCESS: %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"')
if _access_log_format:
    access_log_format = _access_log_format

# The Error log file to write to.
# http://docs.gunicorn.org/en/stable/settings.html#errorlog
_errorlog = os.environ.get('GUNICORN_ERRORLOG', '-')
if _errorlog:
    errorlog = _errorlog

# The granularity of Error log outputs.
# http://docs.gunicorn.org/en/stable/settings.html#errorlog
_loglevel = os.environ.get('GUNICORN_LOGLEVEL', 'info')
if _loglevel:
    loglevel = _loglevel
