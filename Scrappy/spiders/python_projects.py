import string
from scrapy import log
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from Scrappy.items import Project

class Python(CrawlSpider):
    name = 'python'
    allowed_domains = ['freelancer.com']
    start_urls = ['http://www.freelancer.com/jobs/Python']

    rules = (
        Rule(SgmlLinkExtractor(allow=('/jobs/Python/\d*', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('A response from %s just arrived!' % response.url)

        hxs = HtmlXPathSelector(response)
        items = []


        all_projects = hxs.select('//table[@id="project_table_static"]/tbody/tr')

        for project in all_projects:
            all_details = project.select('td')
            item = Project()

            #Get Project Name
            item["name"] = string.strip(" ".join(all_details[0].select('a/text()').extract()))

            #Get Project Description
            item["description"] = all_details[1].select('text()').extract()

            #Get Bids Number
            item["bids"] = all_details[2].select('text()').extract()

            #Get Project Skills
            all_skill = all_details[3].select('a/text()').extract()
            item["skill"] = ", ".join(all_skill)

            #Get Project start date
            item["start"] = all_details[4].select('text()').extract()

            #Get Project budget average
            item["average"] = all_details[6].select('text()').extract()

            items.append(item)

        return items
