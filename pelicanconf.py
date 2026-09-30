import hashlib
import os
import re

AUTHOR = u'- jj'
SITENAME = u'nedopsáno'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'Europe/Prague'
LOCALE = 'cs_CZ.UTF-8'
DEFAULT_LANG = u'cs'
DEFAULT_DATE_FORMAT = "%-d. %-m. %Y"

THEME = 'theme'

# Every poem lives on the single index page, reachable by anchor.
ARTICLE_URL = '#{slug}'
ARTICLE_SAVE_AS = ''
DIRECT_TEMPLATES = ['index', 'nedopsano']
NEDOPSANO_SAVE_AS = 'nedopsano/index.html'
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

# Cloudflare caches style.css for hours but not the HTML, so a changed
# stylesheet needs a new URL: ?v= is a hash of its content.
_CSS = os.path.join(os.path.dirname(__file__), 'theme/static/css/style.css')
with open(_CSS, 'rb') as f:
    CSS_VERSION = hashlib.sha256(f.read()).hexdigest()[:8]


def verse_lines(html):
    """Wrap each verse line in <span class="line"> for the hanging indent.

    ponytail: assumes nl2br's plain <p>…<br>…</p>, which is all a poem is.
    """
    html = html.replace('<p>', '<p><span class="line">').replace('</p>', '</span></p>')
    return re.sub(r'<br>\s*', '</span><span class="line">', html)


JINJA_FILTERS = {'verse_lines': verse_lines}
