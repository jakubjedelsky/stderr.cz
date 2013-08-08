#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### blog info
AUTHOR = u'Jakub Jedelský'
SITENAME = u'stderr'
SITEURL = 'http://g.stderr.cz'

SITESUBTITLE = u'poznámky'
AUTHOR_BIO = u"Správce linuxových serverů v brněnském datacentru, milovník dobré hudby a jídla. Obdivuje ty, co dokáží něco dokázat."

### timezone and l10n
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'

DEFAULT_LANG = u'cs'
DEFAULT_DATE_FORMAT = "%d. %m. %Y"

### feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

### nice urls
ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}.html'

ARTICLE_LANG_URL = '{lang}/{slug}'
ARTICLE_LANG_SAVE_AS = '{lang}/{slug}.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

### static things
STATIC_PATHS = ['images']
FILES_TO_COPY = ( 
        ('extra/robots.txt', 'robots.txt'),
        ('extra/CNAME', 'CNAME'),
    )   

### theme
THEME = 'theme'
DISPLAY_PAGES_ON_MENU = True
SUMMARY_MAX_LENGTH = 80
# pagination
DEFAULT_PAGINATION = 5 

### social things
# socicons
SOCIAL = {
    'twitter': 'https://twitter.com/kubiis',
    'linkedin': 'http://www.linkedin.com/in/jedelsky',
    'github': 'https://github.com/jakubjedelsky',
}
# flattr
FLATTR_ID = 'stderr'
# disqus
DISQUS_SITENAME = 'stderr-cz-blog'
