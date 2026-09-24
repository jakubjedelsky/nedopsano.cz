AUTHOR = u'- jj'
SITENAME = u'nedopsáno'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = u'cs'
DEFAULT_DATE_FORMAT = "%d. %m. %Y"

THEME = 'theme'

# Every poem lives on the single index page, reachable by anchor.
ARTICLE_URL = '#{slug}'
ARTICLE_SAVE_AS = ''
DIRECT_TEMPLATES = ['index']
DEFAULT_PAGINATION = False
PAGE_PATHS = []

# ponytail: emptying *_SAVE_AS beats the `rm -rf` the blog's workflow does.
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

FEED_ALL_ATOM = 'feed.atom.xml'
CATEGORY_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_ATOM = None

# nl2br keeps verse line breaks; overriding MARKDOWN drops Pelican's
# defaults, so meta has to be listed again or metadata parsing breaks.
MARKDOWN = {
    'extensions': [
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
    ],
    'output_format': 'html5',
}

STATIC_PATHS = ['extra/CNAME', 'extra/favicon.ico', 'extra/favicon.svg']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon.svg': {'path': 'favicon.svg'},
}
