# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from djangoApi.models import Match

class MatchItem(DjangoItem):
    django_model = Match

class CrawlingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
