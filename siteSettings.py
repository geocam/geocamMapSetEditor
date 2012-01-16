# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

# siteSettings.py -- site default settings
#
# This contains the default settings for the site-level django app.  This will
# override any application-default settings and define the default set of
# installed applications. This should be a full settings.py file which needs
# minimal overrides by the settings.py file for the application to actually
# function.
#
# As a bare minimum, please edit INSTALLED_APPS!
#
# This file *should* be checked into git.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
import os
import sys
#APP = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
#PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJ_ROOT = os.path.abspath(os.path.dirname(__file__))

SCRIPT_NAME = os.environ['DJANGO_SCRIPT_NAME']  # set in sourceme.sh
USING_DJANGO_DEV_SERVER = ('runserver' in sys.argv)
if USING_DJANGO_DEV_SERVER:
    # django dev server deployment won't work with other SCRIPT_NAME settings
    SCRIPT_NAME = '/'

# Python path is agnostic to what the site-level dir is. It also prefers the
# checked-out version of an app over the standard python install locations.
sys.path.append(PROJ_ROOT)

ADMINS = (
    # ('Trey Smith', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.db'
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJ_ROOT, "build", "media", "")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = SCRIPT_NAME + 'media/'

# Absolute path to the directory that holds data. This is different than media
# in that it's uploaded/processed data that's not needed for the operation of
# the site, but may need to be network-accessible, or be linked to from the
# database. Examples: images, generate kml files, etc.
# Example: "/data/"
DATA_ROOT = os.path.join(PROJ_ROOT, "data", "")

DATA_DIR = DATA_ROOT  # some legacy modules use the DATA_DIR name

# URL that handles the data served from DATA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://data.lawrence.com", "http://example.com/data/"
DATA_URL = SCRIPT_NAME + "data/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = SCRIPT_NAME + 'admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l0+e-mp@uf&f(s_nr(&b#w&tkd9ky&vaw-g*h8o-3pqxuk8lbj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'geocamUtil.middleware.LogErrorsMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'geocamUtil.middleware.SecurityMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'geocamUtil',

    # Put your installed apps here!
    # 'geocamAwesome'
)

GEOCAM_UTIL_SECURITY_ENABLED = not USING_DJANGO_DEV_SERVER
GEOCAM_UTIL_SECURITY_SSL_REQUIRED_BY_DEFAULT = False
GEOCAM_UTIL_SECURITY_REQUIRE_ENCRYPTED_PASSWORDS = False
GEOCAM_UTIL_SECURITY_LOGIN_REQUIRED_BY_DEFAULT = 'write'
