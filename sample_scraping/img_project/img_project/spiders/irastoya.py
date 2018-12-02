# -*- coding: utf-8 -*-
import scrapy

from img_project.items import ImgProjectItem

class IrastoyaSpider(scrapy.Spider):
    name = 'irastoya'
    allowed_domains = ['www.irasutoya.com']
    start_urls = ['https://www.irasutoya.com/']
    # allowed_domains = ['news.yahoo.co.jp/']
    # start_urls = ['https://news.yahoo.co.jp/']

    def parse(self, response):
        item = ImgProjectItem()
        image_urls = []
        for img_url in response.css("img").xpath("@src").extract():
            if (img_url.endswith('jpg') or img_url.endswith('png')) and img_url.startswith('https://'):
                image_urls.append(img_url)
                self.log(f'Saved file {img_url}')
        item['image_urls'] = image_urls
        return item
        

