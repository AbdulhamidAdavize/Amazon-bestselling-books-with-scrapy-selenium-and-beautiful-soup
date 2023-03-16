# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonscrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    rank = scrapy.Field()
    author = scrapy.Field()
    ratings = scrapy.Field()
    cover_type = scrapy.Field()
    no_of_reviews = scrapy.Field()
    year = scrapy.Field()
