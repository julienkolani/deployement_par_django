#!/bin/sh

. /home/app/my_app_venv/bin/activate && /home/app/my_app_venv/bin/python3 /home/app/test_app/manage.py collectstatic --noinput && deactivate