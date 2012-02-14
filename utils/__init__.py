import json
from django.http import HttpResponse

def response_json(response_dict):
    return HttpResponse(json.dumps(response_dict), mimetype='application/javascript')
