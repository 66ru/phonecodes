# Scrapy settings for parser project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os, sys

def setup_django_env(path):
    import imp
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)

    setup_environ(project)

path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(path)
setup_django_env(path)

BOT_NAME = 'parser'
BOT_VERSION = '1.0'

LOG_LEVEL = 'INFO'
SPIDER_MODULES = ['codeparser.spiders']
NEWSPIDER_MODULE = 'codeparser.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'codeparser.pipelines.ParserPipeline',
]


