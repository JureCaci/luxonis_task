# Connect to database and scrape data from sreality.cz
#import psycopg2
#
#con = psycopg2.connect(
#database="devdb",
#user="devuser",
#password="devpass",
#host="db",
#port= '5432'
#)
#
#
#cur = con.cursor()
#result = cur.execute("SELECT REPEAT('Hello', 5)")
#print("Result", result)

import scrapy

class SrealityFlatsSpider(scrapy.Spider):
    name = "sreality_flats"
    start_urls = [
        'https://www.sreality.cz/en/search/for-sale/apartments',
    ]

    def parse(self, response):
        # class= "dir-property-list"
        #class="_2xzMRvpz7TDA2twKCXTS4R"
        # first a tag
        # img tag inside a tag

        # element after class="_2xzMRvpz7TDA2twKCXTS4R"
        # div class="text-wrap"
        # inside span
        # h2>a>span>text
        #span
        #span

        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'