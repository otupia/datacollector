# -*- coding: utf-8 -*-
import scrapy


class CdcSpider(scrapy.Spider):
    name = "cdc"
    allowed_domains = ["cdc.gov"]
    start_urls = (
        'http://www.cdc.gov/',
    )

    def parse(self, response):
        pass
