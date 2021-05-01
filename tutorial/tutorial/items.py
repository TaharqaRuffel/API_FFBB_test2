# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    pass

class MatchItem(scrapy.Item):
    championship = scrapy.Field
    day = scrapy.Field
    match_date = scrapy.Field
    home = scrapy.Field
    visitor = scrapy.Field
    score_home = scrapy.Field
    score_visitor = scrapy.Field
    plan = scrapy.Field