from scrapy import log
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from Scrappy.items import Project

class Django(BaseSpider):
    name = 'django'
    allowed_domains = ['freelancer.com']
    start_urls = ['http://www.freelancer.com/jobs/Django']

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        hxs = HtmlXPathSelector(response)
        items = []


        all_projects = hxs.select('//table[@id="project_table_static"]/tbody/tr')

        for project in all_projects:
            all_details = project.select('td')
            item = Project()

            #Get Project Name
            item["name"] = all_details[0].select('a/text()').extract()

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
