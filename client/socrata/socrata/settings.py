# Scrapy settings for socrata project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'socrata'

SPIDER_MODULES = ['socrata.spiders']
NEWSPIDER_MODULE = 'socrata.spiders'

DOWNLOAD_DELAY = 10
ITEM_PIPELINES = ['socrata.pipelines.SocrataPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'socrata (+http://www.yourdomain.com)'
