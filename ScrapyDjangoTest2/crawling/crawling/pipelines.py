# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import string

from itemadapter import ItemAdapter


# class CrawlingPipeline:
#     def process_item(self, item, spider):
#         return item

from djangoApi.models import Match
import datetime

def clean_created(param):
    return param

def clean_championship(param):
    return param

def clean_day(param):
    return param

def clean_match_date(param):
    return param

def clean_home(param):
    return param

def clean_visitor(param):
    return param

def clean_score_home(param):
    return param

def clean_score_visitor(param):
    return param

def clean_plan(param):
    return param.replace("'","")

class CrawlingPipeline(object):
    def process_item(self, item, spider):
        created = datetime.datetime.now()
        updated = datetime.datetime.now()
        championship = clean_championship(item['championship'])
        day = clean_day(item['day'])
        match_date = clean_match_date(item['match_date'])
        home = clean_home(item['home'])
        visitor = clean_visitor(item['visitor'])
        score_home = clean_score_home(item['score_home'])
        score_visitor = clean_score_visitor(item['score_visitor'])
        plan = clean_plan(item['plan'])

        Match.objects.create(
            created=created,
            updated = updated,
            championship = championship ,
            day = day,
            match_date = match_date,
            home = home,
            visitor = visitor,
            score_home = score_home,
            score_visitor = score_visitor,
            plan = plan
        )

        return item