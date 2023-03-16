# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

import sqlite3


class AmazonscrapePipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.curr = self.conn.cursor()

    def create_connection(self):
        self.conn = sqlite3.connect("books.db")

    def create_table(self):

        self.curr.execute("""
        CREATE TABLE EXIST books_tb(
            title TEXT,
            rank TEXT,
            author TEXT,
            ratings TEXT,
            cover_type VARCHAR 255,
            no_of_reviews TEXT,
            year TEXT 
            )
            """)

    def store_db(self, item):
        self.curr.execute(
            '''INSERT INTO books_tb VALUES (?,?,?,?,?,?,?)''', (

                item['title'],
                item['rank'],
                item['author'],
                item['ratings'],
                item['cover_type'],
                item['no_of_reviews'],
                item['year'])
            )
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
