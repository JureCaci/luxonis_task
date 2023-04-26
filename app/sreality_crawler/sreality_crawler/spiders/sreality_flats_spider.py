import scrapy
from sreality_crawler.items import SrealityFlatItem
from scrapy.exceptions import CloseSpider

class SrealityFlatsSpider(scrapy.Spider):
    handle_httpstatus_list = [403, 404]
    name = "sreality_flats"
    allowed_domains  = ['sreality.cz']
    counter = 0
    max_number_of_items = 500
    start_urls = [
        'https://www.sreality.cz/en/search/for-sale/apartments?_escaped_fragment_=',
    ]

    custom_settings = {
    'LOG_LEVEL': 'DEBUG'
    }
    def parse(self, response):
        sreality_flat_item = SrealityFlatItem()
        for property in response.css('div.dir-property-list > div.property'):
            image_url = property.css("div._2xzMRvpz7TDA2twKCXTS4R > a > img::attr(src)").get()
            print("Image", image_url)
            title = property.css("div.text-wrap > span.basic > h2 > a > span.name::text").get()
            print("Title", title)
            sreality_flat_item['title'] = title
            sreality_flat_item['image_url'] = image_url

            yield sreality_flat_item
            self.counter += 1
            if self.counter >= self.max_number_of_items:
                raise CloseSpider('Processed 500 items')

        next_page = response.css("div.paging > ul.paging-full > li:last-child > a::attr(href)").get()
        next_page += "&_escaped_fragment_="
        print("Next page", next_page)
        if next_page:
            yield response.follow(next_page, callback=self.parse)
