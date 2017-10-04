# -*- coding: utf-8 -*-
import scrapy
import csv
from amazon_scrapy.items import AmazonScrapyItem
from scrapy import Request

class ImagesDownloaderSpider(scrapy.Spider):
    name = 'images_downloader'
    #take urls from file and put urls in a list
    url_list = []
    with open('/users/pavlos/test.csv') as csvfile:
        reader = csv.reader(csvfile,dialect='excel')
        for i,row in enumerate(reader):
            str = ''.join(row)
            print(str)
            url_list.append(str)


    def start_requests(self):
        for i,url in enumerate(self.url_list):
            yield Request(url=url)



    def parse(self, response):
        #item = AmazonScrapyItem()
        #item['image_urls'] = response.url
        yield AmazonScrapyItem(image_urls = [response.url])





