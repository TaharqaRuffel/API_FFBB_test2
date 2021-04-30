import scrapy

MATCH_DAY_LABEL = 'Jour'
MATCH_DATE_LABEL = 'Date'
MATCH_TIME_LABEL = 'Heure'
MATCH_HOME = 'Domicile'
MATCH_VISITOR = 'Visiteur'
MATCH_RESULT = 'Résultat'
MATCH_GYM = 'Salle'


class ffbbSpiderMatch(scrapy.Spider):
    name = "ffbb_match"

    # start_urls = [
    #         'https://resultats.ffbb.com/championnat/equipe/division/b5e6211eeed6b5e621202c272263.html',
    # ]

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

    def parse(self, response):
        # récupérer les numéros des colonnes des champs
        headers = response.css('.titre-bloc td::text').getall()
        headersIndexes = self.getColumnsIndex(headers)

        content = response.css('.altern-2')

        for line in content:
            if len(line.css('.infos_complementaires')) == 0:
                attributs = line.xpath('td//text()').getall()
                yield {
                    'journee': attributs[headersIndexes[MATCH_DAY_LABEL]],
                    'date': attributs[headersIndexes[MATCH_DATE_LABEL]],
                    'heure': attributs[headersIndexes[MATCH_TIME_LABEL]],
                    'domicile': attributs[headersIndexes[MATCH_HOME]],
                    'visiteur': attributs[headersIndexes[MATCH_VISITOR]],
                    'score': attributs[headersIndexes[MATCH_RESULT]],
                    'plan': attributs[headersIndexes[MATCH_GYM]],
                }
        content = response.css('.no-altern-2')

        for line in content:
            if len(line.css('.infos_complementaires')) == 0:
                attributs = line.xpath('td//text()').getall()
                yield {
                    'journee': attributs[headersIndexes[MATCH_DAY_LABEL]],
                    'date': attributs[headersIndexes[MATCH_DATE_LABEL]],
                    'heure': attributs[headersIndexes[MATCH_TIME_LABEL]],
                    'domicile': attributs[headersIndexes[MATCH_HOME]],
                    'visiteur': attributs[headersIndexes[MATCH_VISITOR]],
                    'score': attributs[headersIndexes[MATCH_RESULT]],
                    'plan': attributs[headersIndexes[MATCH_GYM]],
                }

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
