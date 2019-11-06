#!/usr/bin/env python3
import json
from pprint import pprint

import requests
import requests_cache

# Cache for rapid querying that lasts 60 seconds.
requests_cache.install_cache('4plebs_cache', backend='sqlite', expire_after=60)


def gen_index_url(board: str, page: int) -> str:
    return f"http://archive.4plebs.org/_/api/chan/index/?board={board}&page={page}"


def gen_post_url(board: str, postid: int) -> str:
    return f"http://archive.4plebs.org/_/api/chan/post/?board={board}&num={postid}"


def gen_thread_url(board: str, threadid: int) -> str:
    return f"http://archive.4plebs.org/_/api/chan/thread/?board={board}&num={threadid}"


# from https://archive.4plebs.org/_/articles/faq/
POL_PAGE_1_URL = gen_index_url('pol', 1)

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


if __name__ == '__main__':
    result = httpGET_json(POL_PAGE_1_URL)

    postids = result.keys()

    pprint(result)
    pprint(postids)
