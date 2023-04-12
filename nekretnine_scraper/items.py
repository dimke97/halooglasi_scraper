# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NekretnineScraperItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    sqr_m = scrapy.Field()
    room_num = scrapy.Field()
    floor = scrapy.Field()
    description = scrapy.Field()
    publish_date = scrapy.Field()
    ad_owner = scrapy.Field()
    city = scrapy.Field()
    municipality = scrapy.Field()
    suburb = scrapy.Field()
    street = scrapy.Field()
    url_link = scrapy.Field()
