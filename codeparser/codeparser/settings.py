# Scrapy settings for parser project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
import os
import sys


def setup_django_env(path):
    import imp
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('scrapy_settings', [path])
    project = imp.load_module('scrapy_settings', f, filename, desc)

    setup_environ(project)

    from django.core.management.commands import syncdb
    syncdb.Command().execute(noinput=True)
    from django.core.management.commands import flush
    flush.Command().execute(noinput=True)


path = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(path)
setup_django_env(path)

LOG_LEVEL = 'INFO'
SPIDER_MODULES = ['codeparser.spiders']
NEWSPIDER_MODULE = 'codeparser.spiders'

ITEM_PIPELINES = [
    'codeparser.pipelines.ParserPipeline',
]
