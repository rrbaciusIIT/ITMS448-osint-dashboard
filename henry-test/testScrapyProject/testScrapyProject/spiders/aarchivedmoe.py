# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from pprint import pprint


class AArchivedMoeSpider(scrapy.Spider):
    name = 'archived.moe'
    allowed_domains = ['archived.moe']
    start_urls = ['https://archived.moe/pol/']

    POST_CONTROLS_SELECTOR = 'header > .post_data > .post_controls'

    def parse(self, response):
        print("Hi! I'm parsing a response!")

        for item in response.css(self.POST_CONTROLS_SELECTOR):
            item: Selector

            # print("Here's the whole thing:")
            # pprint(item.get())

            print("rexp for thread URLs:")
            pprint(item.re(r'href=".+?/thread/\d+?/"'))

            # post_url = item.re('').get()
            #
            #
            # print("Just the URL link:")
            # pprint(post_url)
