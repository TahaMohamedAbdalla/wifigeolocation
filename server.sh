#!/usr/bin/sh
sudo gunicorn --workers=3 -b 127.0.0.1:8883 manage:app