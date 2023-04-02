#!/user/bin/env bash

set -o errexit

pip intstall -r requirements.txt

python manage.py collectstatic --no-input
puthon manage.py migrate