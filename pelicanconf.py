AUTHOR = "Andrew Tinits"
SITENAME = "Andrew Tinits"
SITEURL = "https://tinits.com"
TIMEZONE = "America/Toronto"
DEFAULT_LANG = "en"

THEME = "simple"
THEME_TEMPLATES_OVERRIDES = ["templates"]
TYPOGRIFY = True

PATH = "content"
STATIC_PATHS = ["CNAME", "favicon.ico", "robots.txt", "css", "images", "files"]
DIRECT_TEMPLATES = ["index"]
SLUGIFY_SOURCE = "basename"
ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
