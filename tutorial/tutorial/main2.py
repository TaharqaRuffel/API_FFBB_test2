import json
from scrapy.crawler import CrawlerProcess
from tutorial.tutorial.spiders.ffbb_spider_championships import ffbbSpiderChampionships

CHAMPIONSHIPS_TEMP = "championshipsTmp"
CHAMPIONSHIPS_TEMP_EXTENSION = "jl"
CHAMPIONSHIPS_TEMP_FILE = CHAMPIONSHIPS_TEMP + '.' + CHAMPIONSHIPS_TEMP_EXTENSION
DIVISION_FOLDER = "https://resultats.ffbb.com/championnat/equipe/division"
DEFAULT_EXT = ".html"

def changerRencontresResultatsEquipe(championshipIndex):
    return DIVISION_FOLDER + "/" + championshipIndex + DEFAULT_EXT


def convertJl(fileJl):
    newArray = []
    with open(fileJl, 'r') as f:
        for line in f:
            newArray.append(json.loads(line))
    return newArray


def getListUrlsChampionship():
    process = CrawlerProcess(settings={
        "FEEDS": {
            CHAMPIONSHIPS_TEMP_FILE: {"format": CHAMPIONSHIPS_TEMP_EXTENSION},
        },
    })

    process.crawl(ffbbSpiderChampionships, start_urls=['https://resultats.ffbb.com/championnat/equipe/2263.html'])
    process.start()

    lines = convertJl(CHAMPIONSHIPS_TEMP_FILE)

    listUrls = []

    for line in lines:
        listUrls.append(changerRencontresResultatsEquipe(line['index']))
    return listUrls
