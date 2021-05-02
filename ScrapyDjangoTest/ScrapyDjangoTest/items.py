# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from matches.models import Match


class ScrapydjangotestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# class BrandsItem(DjangoItem):
#    django_model = Product
#    stock = scrapy.Field() # You can still add extra fields

class MatchItem(DjangoItem):
    django_model = Match
    created = scrapy.Field()
    updated = scrapy.Field()
    championship = scrapy.Field()
    day = scrapy.Field()
    match_date = scrapy.Field()
    home = scrapy.Field()
    visitor = scrapy.Field()
    score_home = scrapy.Field()
    score_visitor = scrapy.Field()
    plan = scrapy.Field()