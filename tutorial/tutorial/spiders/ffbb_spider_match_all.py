from datetime import datetime
import json
import re
import scrapy

ATTR_MATCH_CHAMPIONSHIP_ID = 'ChampionnatId'

REGEX_WITHIN_CURLY_BRACKETS = "\{(.*?)\}"
REGEX_WITHIN_SINGLE_QUOTE = "\'(.*?)\'"

ATTR_MATCH_DAYS = 'journee'
ATTR_MATCH_DATE = 'date'
ATTR_MATCH_TIME = 'heure'
ATTR_MATCH_HOME = 'domicile'
ATTR_MATCH_VISITOR = 'visiteur'
ATTR_MATCH_SCORE_HOME = 'score_domicile'
ATTR_MATCH_SCORE_VISITOR = 'score_visiteur'
ATTR_MATCH_GYM = 'plan'

CSS_CLASS_LINE_MATCH_2 = '.no-altern-2'
CSS_CLASS_LINE_MATCH_1 = '.altern-2'
CSS_INFOS_COMPLEMENTAIRES = '.infos_complementaires'
XPATH_TD_TEXT = 'td//text()'

MATCH_DAY_LABEL = 'Jour'
MATCH_DATE_LABEL = 'Date'
MATCH_TIME_LABEL = 'Heure'
MATCH_HOME = 'Domicile'
MATCH_VISITOR = 'Visiteur'
MATCH_RESULT = 'Résultat'
MATCH_GYM = 'Salle'
DIVISION_FOLDER = "https://resultats.ffbb.com/championnat/equipe/division"
DEFAULT_EXT = ".html"


class ffbbSpiderMatchAll(scrapy.Spider):
    name = "ffbb_match_all"
    #start_urls = ['https://resultats.ffbb.com/championnat/equipe/2263.html']


    def parse(self, response):

        content = response.css('#idCompetitionsSelect option')

        for i in range(len(content)):
            next_team = self.changerRencontresResultatsEquipe(content[i].attrib['value'])
            next_team = response.urljoin(next_team)
            yield scrapy.Request(next_team, callback=self.parseMatches)

    def parseMatches(self, response):

        # récupérer les numéros des colonnes des champs
        headers = response.css('.titre-bloc td::text').getall()
        headersIndexes = self.getColumnsIndex(headers)
        championshipId = self.getChampionshipId(response)



        content = response.css(CSS_CLASS_LINE_MATCH_1)

        for line in content:
            if len(line.css(CSS_INFOS_COMPLEMENTAIRES)) == 0:
                attributs = line.xpath(XPATH_TD_TEXT).getall()
                gymId = self.getGymId(line.css('.poplight').attrib["href"]).replace("'", "")
                if attributs[headersIndexes[MATCH_RESULT]] != "-":
                    score = attributs[headersIndexes[MATCH_RESULT]].split(" - ")
                else:
                    score = ["0", "0"]

                yield {
                    ATTR_MATCH_CHAMPIONSHIP_ID: championshipId,
                    ATTR_MATCH_DAYS: int(attributs[headersIndexes[MATCH_DAY_LABEL]]),
                    ATTR_MATCH_DATE: datetime.strptime(attributs[headersIndexes[MATCH_DATE_LABEL]] + ' ' + attributs[headersIndexes[MATCH_TIME_LABEL]] + ':00',  '%d/%m/%Y %H:%M:%S'),
                    ATTR_MATCH_HOME: attributs[headersIndexes[MATCH_HOME]],
                    ATTR_MATCH_VISITOR: attributs[headersIndexes[MATCH_VISITOR]],
                    ATTR_MATCH_SCORE_HOME: int(score[0]),
                    ATTR_MATCH_SCORE_VISITOR: int(score[1]),
                    ATTR_MATCH_GYM: gymId,
                }
        content = response.css(CSS_CLASS_LINE_MATCH_2)

        for line in content:
            if len(line.css(CSS_INFOS_COMPLEMENTAIRES)) == 0:
                attributs = line.xpath(XPATH_TD_TEXT).getall()
                gymId = self.getGymId(line.css('.poplight').attrib["href"])

                if attributs[headersIndexes[MATCH_RESULT]] != "-":
                    score = attributs[headersIndexes[MATCH_RESULT]].split(" - ")
                else:
                    score = [0,0]

                yield {
                    ATTR_MATCH_CHAMPIONSHIP_ID: championshipId,
                    ATTR_MATCH_DAYS: int(attributs[headersIndexes[MATCH_DAY_LABEL]]),
                    ATTR_MATCH_DATE: datetime.strptime(attributs[headersIndexes[MATCH_DATE_LABEL]] + ' ' + attributs[headersIndexes[MATCH_TIME_LABEL]] + ':00',
                                                       '%d/%m/%Y %H:%M:%S'),
                    ATTR_MATCH_HOME: attributs[headersIndexes[MATCH_HOME]],
                    ATTR_MATCH_VISITOR: attributs[headersIndexes[MATCH_VISITOR]],
                    ATTR_MATCH_SCORE_HOME: int(score[0]),
                    ATTR_MATCH_SCORE_VISITOR: int(score[1]),
                    ATTR_MATCH_GYM: gymId,
                }

    def getColumnsIndex(self, headers):
        headersIndexes = {}
        for index in range(len(headers)):
            if headers[index] == MATCH_DAY_LABEL:
                headersIndexes[MATCH_DAY_LABEL] = index
            elif headers[index] == MATCH_DATE_LABEL:
                headersIndexes[MATCH_DATE_LABEL] = index
            elif headers[index] == MATCH_TIME_LABEL:
                headersIndexes[MATCH_TIME_LABEL] = index
            elif headers[index] == MATCH_HOME:
                headersIndexes[MATCH_HOME] = index
            elif headers[index] == MATCH_VISITOR:
                headersIndexes[MATCH_VISITOR] = index
            elif headers[index] == MATCH_RESULT:
                headersIndexes[MATCH_RESULT] = index
            elif headers[index] == MATCH_GYM:
                headersIndexes[MATCH_GYM] = index
        return headersIndexes

    def changerRencontresResultatsEquipe(self, championshipIndex):
        return DIVISION_FOLDER + "/" + championshipIndex + DEFAULT_EXT

    def getGymId(self, string):
        gymId = re.search(REGEX_WITHIN_SINGLE_QUOTE, string).group()
        return gymId

    def getChampionshipId(self, response):
        base = response.request.url
        x = base.rfind("/") + 1
        y = base.rfind(".")
        return base[x:y]

    # def parseGym(self, response):
    #     gym_js_script = response.css('head script::text').getall()
    #     result = re.search(REGEX_WITHIN_CURLY_BRACKETS, gym_js_script)
    #     print(result[0])
    #
    #     objet_json = json.loads(result[0])
    #     print(objet_json['longitude'])
    #
    #     self.gym = objet_json

