# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from pprint import pprint


class A4chanSpider(scrapy.Spider):
    name = '4chan'
    allowed_domains = ['archived.moe']
    start_urls = ['https://archived.moe/pol/']

    POST_CONTROLS_SELECTOR = 'header > .post_data > .post_controls'

    def parse(self, response):
        print("Hi! I'm parsing a response!")

        for item in response.css(self.POST_CONTROLS_SELECTOR):
            item: Selector

            print("Here's the whole thing:")
            pprint(item.get())

            # post_url = item.re('').get()
            #
            #
            # print("Just the URL link:")
            # pprint(post_url)
