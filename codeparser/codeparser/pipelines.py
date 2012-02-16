from codes.models import Operator

class ParserPipeline(object):
    def process_item(self, item, spider):
        operator = Operator(**item)
        operator.save()
        return item
