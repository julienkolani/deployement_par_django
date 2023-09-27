#!/bin/sh

. /home/app/my_app_venv/bin/activate && python /home/app/test_app/manage.py collectstatic --noinput && deactivate

# Exécute unitd en arrière-plan et redirige la sortie vers /home/app/out.log
unitd --no-daemon --control unix:/var/run/control.unit.sock > /home/app/out.log 2>&1 &

# Exécute curl
curl -X PUT --data-binary @/etc/unit/django.config --unix-socket /run/control.unit.sock http://localhost/config

tail -f /dev/null
