#!/usr/bin/env python3

import requests
import requests_cache

# Cache for rapid querying that lasts 60 seconds.
requests_cache.install_cache('4plebs_cache', backend='sqlite', expire_after=60)


# from https://archive.4plebs.org/_/articles/faq/
POL_PAGE_1_URL = 'http://archive.4plebs.org/_/api/chan/index/?board=pol&page=1'

print("Wow! Look at all this Web API stuff!")


def testCacheWorks():
    """This should not take 50 seconds if the cache works."""
    print("Testing if the request cache works.")
    for i in range(0, 10):
        print(requests.get('http://httpbin.org/delay/5'))


testCacheWorks()