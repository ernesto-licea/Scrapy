# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrappyItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class Project(Item):
    name = Field()
    bids = Field()
    skill = Field()
    average = Field()
    description = Field()
    start = Field()

class Users(Item):
    username = Field()
    name = Field()
    last_name = Field()
    phone = Field()
    department = Field()

