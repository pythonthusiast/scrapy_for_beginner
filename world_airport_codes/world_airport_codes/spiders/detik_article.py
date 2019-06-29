# -*- coding: utf-8 -*-
import scrapy


class DetikArticleSpider(scrapy.Spider):
    name = 'detik_article'
    allowed_domains = ['www.detik.com']
    start_urls = ['http://www.detik.com/']

    def parse(self, response):
        data = []

        data.append({'title': 'title article', 'url': 'url article'})
        return data
