# Scrapy settings for Scrappy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'Scrappy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['Scrappy.spiders']
NEWSPIDER_MODULE = 'Scrappy.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

FEED_URI = 'file:///home/ernesto/projects_%(name)s.csv'
FEED_FORMAT = 'csv'