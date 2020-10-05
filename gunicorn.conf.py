bind = "0.0.0.0:5000"
workers = 4
# Access log - records incoming HTTP requests
accesslog = "logs/gunicorn.log"
# Error log - records Gunicorn server goings-on
errorlog = "logs/gunicorn.log"
capture_output = True
# How verbose the Gunicorn error logs should be
loglevel = "info"
