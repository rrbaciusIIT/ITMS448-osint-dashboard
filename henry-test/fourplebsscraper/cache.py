import requests_cache


def install_4plebs_cache(expire=60):
    """Enables a cache for requests."""
    # Cache for rapid querying that lasts 60 seconds.
    requests_cache.install_cache('4plebs_scraper_cache', backend='sqlite', expire_after=expire)
