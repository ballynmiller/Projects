# default settings to be imported into settings files. 
class DJANGO_SETTINGS: 
    DEFAULT={
        'LANDING':False,
        'CONSUMER_KEY':'#',
        'SUBSCRIBER_FORM':False,
        'REGISTER':False, 
        'SHOPPING':False,
        'EMAIL_ADDRESS':'#',
        'EMAIL_HOST':'localhost',
        'EMAIL_PORT':25,
        'SHOPPING':False,
        'SUBSCRIBER_FORM':False,
        'TWITTER':False,
        'REGISTER':False,
        'TWITTER_NAME':'#',
        'AUTH_TOKEN':'#',
        'AUTH_SECRET':'#',
        'BANNER_DIMENSIONS':'600x400',
        "TEMPLATE_CONTEXT_PROCESSORS":(
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            "django.core.context_processors.static",
            "django.contrib.messages.context_processors.messages"
        ),
        "INSTALLED_APPS":(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.flatpages',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.admin',
            'websites.ads',
            'websites.content',
            'websites.contact',
        ),
        "LOGGING" : {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'mail_admins': {
                    'level': 'ERROR',
                    'class': 'django.utils.log.AdminEmailHandler'
                }
            },
            'loggers': {
                'django.request': {
                    'handlers': ['mail_admins'],
                    'level': 'ERROR',
                    'propagate': True,
                },
            },
        },
        "TEMPLATE_CONTEXT_PROCESSORS":(
            "django.contrib.auth.context_processors.auth",
            "django.core.context_processors.debug",
            "django.core.context_processors.i18n",
            "django.core.context_processors.media",
            "django.core.context_processors.static",
            "django.contrib.messages.context_processors.messages"
        ),
        "INSTALLED_APPS":(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.flatpages',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'django.contrib.admin',
            'websites.ads',
            'websites.content',
            'websites.contact',
            'websites.shopping',
        ),
        "ROOT_URLCONF":'urls',
        "TEMPLATE_LOADERS":(
          'django.template.loaders.filesystem.Loader',
          'django.template.loaders.app_directories.Loader',
        ),
        "MIDDLEWARE_CLASSES":(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
        ),
        "TIME_ZONE":'America/Chicago',
        "LANGUAGE_CODE":'en-us',
        "SITE_ID":1,
        "USE_I18N":True,
        "USE_L10N":True,
        "MEDIA_ROOT":'/uploads/',
        "MEDIA_URL":"http://media.illustrious-designs.com/",
        "STATIC_ROOT":'',
        "STATIC_URL":'http://media.illustrious-designs.com/static/',
        "STATICFILES_FINDERS":(
            'django.contrib.staticfiles.finders.FileSystemFinder',
            'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        ),
        "SECRET_KEY":'*y&%1zxllp%4r^*x^h6lo^vk3cr+3l%xo5e)^0^p63*b2t_2p^',
        "ADMINS":(),
    }
    DEBUG_SETTINGS=DEFAULT.copy()
    DEBUG_SETTINGS.update({
        "MEDIA_URL":"http://ballynmedia.com/",
        "STATIC_URL":"http://ballynmedia.com/static/",
    })
