#!/usr/bin/sh
sudo gunicorn --workers=3  manage:app