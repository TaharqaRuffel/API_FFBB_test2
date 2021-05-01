import scrapy


class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    tags = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)


class MatchItem(scrapy.Item):
    championship = scrapy.Field()
    day = scrapy.Field()
    match_date = scrapy.Field()
    home = scrapy.Field()
    visitor = scrapy.Field()
    score_home = scrapy.Field()
    score_visitor = scrapy.Field()
    plan = scrapy.Field()


product = Product(name='Desktop PC', price=1000)
print(product)

item = MatchItem(championship='test',day=1)
print(item.keys())
