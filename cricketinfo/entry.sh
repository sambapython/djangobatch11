#!/bin/bash
gunicorn --bind 0.0.0.0:8000 cricketinfo.wsgi --workers=3
service nginx reload
service nginx stop
service nginx start