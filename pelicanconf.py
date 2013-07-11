#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jakub Jedelský'
SITENAME = u'stderr'
SITEURL = 'http://g.stderr.cz'

TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'

DEFAULT_LANG = u'cs'
DEFAULT_DATE_FORMAT = "%d. %m. %Y"

# Feeds will come later
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# pagination
DEFAULT_PAGINATION = 5 
SUMMARY_MAX_LENGTH = 80

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

ARTICLE_LANG_URL = '{lang}/{slug}'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

FILES_TO_COPY = ( 
        ('extra/robots.txt', 'robots.txt'),
        ('extra/CNAME', 'CNAME'),
    )   

# Theme
THEME = 'theme'
SITESUBTITLE = u'poznámky'
AUTHOR_BIO = u"Správce linuxových serverů v brněnském datacentru, milovník dobré hudby a jídla. Obdivuje ty, co dokáží něco dokázat."

DISPLAY_PAGES_ON_MENU = True

SOCIAL = {
    'twitter': 'https://twitter.com/kubiis',
    'linkedin': 'http://www.linkedin.com/in/jedelsky',
    'github': 'https://github.com/jakubjedelsky',
}

FLATTR_ID = 'stderr'
