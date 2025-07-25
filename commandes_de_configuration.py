readme_info = f"""\
python readme_am_info.py

python verification_deployement.py

Unit list config : 

curl  --unix-socket /run/control.unit.sock http://localhost/config/

Config apply : 

curl -X PUT --data-binary @/etc/unit/django.config --unix-socket /run/control.unit.sock  http://localhost/config

Config log : 

curl -X PUT -d '"/var/log/access.log"' \
       --unix-socket /run/control.unit.sock \
       http://localhost/config/access_log
"""

print(readme_info)
