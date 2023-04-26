from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sreality_crawler.spiders.sreality_flats_spider import SrealityFlatsSpider


process = CrawlerProcess(get_project_settings())
process.crawl(SrealityFlatsSpider)
process.start()