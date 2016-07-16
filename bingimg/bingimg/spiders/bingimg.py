# coding=utf-8
import scrapy, psycopg2, re
import json
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class searchedImg(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    source_html_url = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    desc = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

def getCrawlUrl():
    # conn = psycopg2.connect(host=settings.DB_IP, port=5432, user='otupia', password="Dittowen27", database='cn_feature')
    # cur = conn.cursor()
    # cur.execute("SELECT * FROM food_restaurant where process_status = '0' order by id limit 1;")
    # code = cur.fetchone()[9]
    # cur.execute("update food_restaurant set process_status = '1' where code = %s",[code])
    # conn.commit()
    # cur.close()
    # conn.close()
    test_words = ['装修']
    print "-" * 50
    for w in test_words :
        print "http://cn.bing.com/images/search?q=%s" % w
        yield "http://cn.bing.com/images/search?q=%s" % w

class dazhongSpider(scrapy.Spider):
    name = "bingimg"
    # allowed_domains = ["www.dianping.com","qcloud.dpfile.com","www.dpfile.com"]
    # start_urls = []

    def start_requests(self):
        for url in getCrawlUrl():
            yield self.make_requests_from_url(url)

    def parse(self, response):
        self.logger.info('Hi, this is an img search page! %s', response.url)
        img = searchedImg()
        print(response.xpath("//div[@class='dg_u']//a").extract())
        print(len(response.xpath("//div[@class='dg_u']//a")))
        yield img


if __name__ == "__main__":
    print getCrawlUrl()
