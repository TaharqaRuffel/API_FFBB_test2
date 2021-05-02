import re
from datetime import datetime

import scrapy
from crawling.items import MatchItem

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
    start_urls = ['https://resultats.ffbb.com/championnat/equipe/2263.html']
    response = ""

    def parse(self, response):
        self.response = response
        content = response.css('#idCompetitionsSelect option')

        for i in range(len(content)):
            next_team = self.changerRencontresResultatsEquipe(content[i].attrib['value'])
            next_team = response.urljoin(next_team)
            yield scrapy.Request(next_team, callback=self.parse_matches)

    def parse_matches(self, response):

        # récupérer les numéros des colonnes des champs
        headers = response.css('.titre-bloc td::text').getall()
        headers_indexes = self.get_columns_index(headers)

        # récupérer l'identifiant du championnat
        championship_id = self.getChampionshipId(response)

        # récupérer l'ensemble des matchItems paires
        items = self.get_match_item(response, headers_indexes, championship_id, CSS_CLASS_LINE_MATCH_1)

        # récupérer l'ensemble des matchItems impaires
        items = self.get_match_item(response, headers_indexes, championship_id, CSS_CLASS_LINE_MATCH_2)

        # enregistrer chaque matchItem
        for item in items:
            yield item

    def get_match_item(self, response: scrapy.http.Response, headers_indexes: dict[str, int], championship_id: str,
                       classCss: str) -> list[MatchItem]:
        """
        @param response: httpResponse
        @param headers_indexes: headers
        @param championship_id: id of the championship
        @param classCss: name of the css class to track
        @return: list of matchItems
        """
        items = []
        content = response.css(classCss)

        for line in content:
            if len(line.css(CSS_INFOS_COMPLEMENTAIRES)) == 0:

                attributs = line.xpath(XPATH_TD_TEXT).getall()
                gym_id = self.getGymId(line.css('.poplight').attrib["href"])

                if attributs[headers_indexes[MATCH_RESULT]] != "-":
                    score = attributs[headers_indexes[MATCH_RESULT]].split(" - ")
                else:
                    score = [0, 0]

                item = MatchItem()
                item['championship'] = championship_id
                item['day'] = int(attributs[headers_indexes[MATCH_DAY_LABEL]])
                item['match_date'] = datetime.strptime(
                    attributs[headers_indexes[MATCH_DATE_LABEL]] + ' ' + attributs[
                        headers_indexes[MATCH_TIME_LABEL]] + ':00', '%d/%m/%Y %H:%M:%S')
                item['home'] = attributs[headers_indexes[MATCH_HOME]]
                item['visitor'] = attributs[headers_indexes[MATCH_VISITOR]]
                item['score_home'] = int(score[0])
                item['score_visitor'] = int(score[1])
                item['plan'] = gym_id

                items.append(item)

        return items

    def get_columns_index(self, headers):
        headers_indexes = {}
        for index in range(len(headers)):
            if headers[index] == MATCH_DAY_LABEL:
                headers_indexes[MATCH_DAY_LABEL] = index
            elif headers[index] == MATCH_DATE_LABEL:
                headers_indexes[MATCH_DATE_LABEL] = index
            elif headers[index] == MATCH_TIME_LABEL:
                headers_indexes[MATCH_TIME_LABEL] = index
            elif headers[index] == MATCH_HOME:
                headers_indexes[MATCH_HOME] = index
            elif headers[index] == MATCH_VISITOR:
                headers_indexes[MATCH_VISITOR] = index
            elif headers[index] == MATCH_RESULT:
                headers_indexes[MATCH_RESULT] = index
            elif headers[index] == MATCH_GYM:
                headers_indexes[MATCH_GYM] = index
        return headers_indexes

    def changerRencontresResultatsEquipe(self, championshipIndex):
        return DIVISION_FOLDER + "/" + championshipIndex + DEFAULT_EXT

    def getGymId(self, string):
        gym_id = re.search(REGEX_WITHIN_SINGLE_QUOTE, string).group()
        return gym_id

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
