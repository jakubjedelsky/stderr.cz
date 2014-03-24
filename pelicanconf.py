#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

### blog info
AUTHOR = u'Jakub Jedelský'
SITENAME = u'stderr'
#SITEURL = 'http://stderr.cz'
SITEURL = 'http://localhost:8000'

SITESUBTITLE = u'poznámky'
AUTHOR_BIO = u"Jsem ta Ops část z DevOps týmu. V <a href='http://www.gooddata.com'>GoodData</a> ROLAP dbám o to, aby všechny databáze běžely a data se lehce nahrávala."

### timezone and l10n
TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'

DEFAULT_LANG = u'cs'
DEFAULT_DATE_FORMAT = "%d. %m. %Y"

### feeds
FEED_ALL_ATOM = 'feed.atom.xml'
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
TWITTER_NAME = 'kubiis'
# flattr
FLATTR_ID = 'stderr'
# disqus
DISQUS_SITENAME = 'stderr-cz-blog'
# GA
GOOGLE_ANALYTICS = 'UA-44139591-1'
