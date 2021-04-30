from scrapy.crawler import CrawlerProcess
from scrapy import Spider


class ffbbSpiderChampionships(Spider):
    name = "ffbb_championships"

    def parse(self, response):
        content = response.css('#idCompetitionsSelect option')

        for i in range(len(content)):
            yield {
                'index': content[i].attrib['value'],
            }
