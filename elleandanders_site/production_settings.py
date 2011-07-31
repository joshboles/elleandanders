from settings import *

MIDDLEWARE_CLASSES += ['elleandanders_site.middleware.NoWWW']

DEBUG = False
CACHE_MIDDLEWARE_SECONDS = 60 * 60 * 24 * 365 * 10 # 10 Years, not correct for leaps