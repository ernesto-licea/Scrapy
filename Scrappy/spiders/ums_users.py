import string
from scrapy import log
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from Scrappy.items import Project, Users

#Prueba
class Python(BaseSpider):
    name = 'ums'
    allowed_domains = ['cnic.edu.cu']
    start_urls = ['http://ums.cnic.edu.cu/admin/accounts/account/']



    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        logout = hxs.select('//div[@id="user-tools"]').select("a[position()=3]/text()").extract()

        if not logout:
            return self.login(response)
        else:
            return self.parse_page(response)


    def login(self,response):
        return [FormRequest.from_response(response,
                    formdata={'username': 'ernesto', 'password': 'marioneta.ums'},
                    callback=self.parse)]

    def parse_page(self,response):
        print "entro"
        hxs = HtmlXPathSelector(response)
        rows = hxs.select('//tr[contains(@class,"row")]')
        print len(rows)
        items = []


        for row in rows:
            item = Users()

            #Get username
            item['username'] = string.strip(" ".join( row.select('th/a/text()').extract() ))

            data = row.select("td")

            #Get Name
            item['name'] = string.strip(" ".join(data[2].select('text()').extract()))

            #Get Last Name
            item['last_name'] = string.strip(" ".join(data[3].select('text()').extract()))

            #Get phone
            item['phone'] = string.strip(" ".join(data[4].select('text()').extract()))

            #Get department
            item['department'] = string.strip(" ".join(data[5].select('text()').extract()))

            items.append(item)
        return items





















