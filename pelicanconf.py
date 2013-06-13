#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jakub Jedelsky'
SITENAME = u'/dev/stderr'
SITEURL = ''

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

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

ARTICLE_LANG_URL = '{lang}/{slug}'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

FILES_TO_COPY = ( 
        ('extra/robots.txt', 'robots.txt'),
        ('extra/CNAME', 'CNAME'),
    )   

