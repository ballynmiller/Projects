from default_settings import DJANGO_SETTINGS
globals().update(DJANGO_SETTINGS.DEFAULT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'jakore',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
TEMPLATE_DIRS = (
        "../websites/templates/personal/jakore",
        "../websites/templates",
        "../websites"
)
SHOPPING=True
SUBSCRIBER_FORM=True
REGISTER=True
TWITTER_NAME='jakoreco'
EMAIL_ADDRESS='jakore.llc.22@gmail.com'
CONSUMER_KEY='noMU7BHufe4bDoDGj1YZyA'
CONSUMER_SECRET='JEZRFmas5Z0EfQxwdVISMaPm282zxTuxfE7qDvgqPxw'
AUTH_TOKEN='25372355-01yyYUgzpkqeDuxbz2YMEkygDaxztDMBvNmGvDXfs'
AUTH_SECRET='ptDC7xf75R4IBTx1fcbbWGuY3vqAnr3G2ggbfFfYPE'
BANNER_DIMENSIONS='540x351'
MEDIA_URL="http://www.jakore.com/"
STATIC_URL="http://www.jakore.com/static/"
