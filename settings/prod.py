from settings.base import *
from settings.base import SECRET_KEY
from settings.base import SITE_PASSWORD

DEBUG = False

ALLOWED_HOSTS = ["https://iph2-puzzlord-34c662c2c86a.herokuapp.com"]

# security checks
assert SECRET_KEY != "FIXME_SECRET_KEY_GOES_HERE"
assert SITE_PASSWORD != "FIXME_PASSWORD_GOES_HERE"
