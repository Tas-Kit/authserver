from authserver.settings.basic import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b9rcz^eu7sx%rs3%e=wu_s!gs4)a7p42!=kuj)bbfva1v0d^ju'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
JWT_AUTH['JWT_PRIVATE_KEY'] = open('authserver/settings/dev.key').read()
JWT_AUTH['JWT_PUBLIC_KEY'] = open('authserver/settings/dev.key.pub').read()
