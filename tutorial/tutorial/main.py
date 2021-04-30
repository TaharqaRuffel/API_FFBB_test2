from scrapy.crawler import CrawlerProcess
from tutorial.tutorial.spiders.ffbb_spider_match_all import ffbbSpiderMatchAll

process = CrawlerProcess(settings={
    "FEEDS": {
        "items.jl": {"format": "jl"},
    },
})

process.crawl(ffbbSpiderMatchAll, start_urls=['https://resultats.ffbb.com/championnat/equipe/2263.html'])

process.start()
