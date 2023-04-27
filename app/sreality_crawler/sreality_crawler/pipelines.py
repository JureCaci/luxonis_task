# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityCrawlerPostgresPipeline:
    def open_spider(self, spider):
        database = "devdb"
        user = "devuser"
        password = "devpass"
        host = "db"
        port = '5432'
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        try:
            self.cur.execute("""
            INSERT INTO sreality_flats (title, image_url) VALUES (%(title)s, %(image_url)s)
            """, item)
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
