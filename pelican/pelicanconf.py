#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kathleen Burnett'
SITENAME = u'Learning As I Go'
SITEURL = 'http://kmb232.github.io'
THEME= 'themes/gum/'

PATH = 'content'


TIMEZONE = 'Europe/Paris'
DEFAULT_DATE = "fs"

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Nats', 'http://nationals.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Website', 'http://kmb232.github.io'),
          ('Email', 'mailto:kathleenmburnett@gmail.com'),
          ('Twitter', 'http://www.twitter.com/kmb232'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
