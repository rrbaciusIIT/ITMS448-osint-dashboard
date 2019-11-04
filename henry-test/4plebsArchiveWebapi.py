#!/usr/bin/env python3
import json
from pprint import pprint

import requests
import requests_cache

# Cache for rapid querying that lasts 60 seconds.
requests_cache.install_cache('4plebs_cache', backend='sqlite', expire_after=60)

# from https://archive.4plebs.org/_/articles/faq/
POL_PAGE_1_URL = 'http://archive.4plebs.org/_/api/chan/index/?board=pol&page=1'
TOTALLY_LEGIT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36'
}

print("Wow! Look at all this Web API stuff!")


def httpGET_json(url: str) -> dict:
    """Given a URL, request content via HTTP GET and return the JSON object the request provides."""
    response = requests.get(url, headers=TOTALLY_LEGIT_HEADERS)

    data = (response.json())

    return data


def testCacheWorks():
    """This should not take 50 seconds if the cache works."""
    print("Testing if the request cache works.")
    for i in range(0, 10):
        print(requests.get('http://httpbin.org/delay/5'))


pprint(httpGET_json(POL_PAGE_1_URL))
