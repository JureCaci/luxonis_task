# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class SrealityCrawlerPostgresPipeline:

    def __init__(self):
        database = "devdb"
        user = "devuser"
        password = "devpass"
        host = "db"
        port = '5432'
        self.connection = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cur = self.connection.cursor()
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS sreality_flats(
            id SERIAL PRIMARY KEY,
            title TEXT,
            image_url TEXT
        )
        """)

    def process_item(self, item, spider):
        self.cur.execute("""
        INSERT INTO sreality_flats (title, image_url) VALUES (%(title)s, %(image_url)s)
        """, item)
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
