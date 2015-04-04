from default_settings import DJANGO_SETTINGS
globals().update(DJANGO_SETTINGS.DEFAULT)

DEBUG = False
TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'jakore', 
        'USER': 'root',
        'PASSWORD': '{PASSWORD}',
        'HOST': '',
        'PORT': '',
    }
}
TEMPLATE_DIRS = (
        "websites/templates/personal/jakore",
        "websites/templates",
)
SHOPPING=True
SUBSCRIBER_FORM=True
REGISTER=True
TWITTER_NAME='jakoreco'
EMAIL_ADDRESS='jakore.llc.22@gmail.com'
EMAIL_HOST_USER='ballyn.miller@gmail.com'
EMAIL_HOST_PASSWORD='{EMAIL_PASSWORD}'
EMAIL_USE_TLS=True
CONSUMER_KEY='noMU7BHufe4bDoDGj1YZyA'
CONSUMER_SECRET='JEZRFmas5Z0EfQxwdVISMaPm282zxTuxfE7qDvgqPxw'
AUTH_TOKEN='25372355-01yyYUgzpkqeDuxbz2YMEkygDaxztDMBvNmGvDXfs'
AUTH_SECRET='ptDC7xf75R4IBTx1fcbbWGuY3vqAnr3G2ggbfFfYPE'
BANNER_DIMENSIONS='540x351'
MEDIA_URL="http://beta.jakore.com/"
STATIC_URL="http://beta.jakore.com/static/"
ROOT_URLCONF='websites.urls'
ALLOWED_HOSTS = ['.jakore.com']
