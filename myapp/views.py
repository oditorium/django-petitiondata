from django.http import HttpResponse

import requests
import json

def hello(request):
    return HttpResponse('Hello World!')

def by_constituency(request):
    r = requests.get('https://petition.parliament.uk/petitions/131215.json')
    dctd = json.loads(r.text)
    sigs_by_const_s = "\n".join([
        '"{}","{}","{}","{}"'.format(i['name'], i['ons_code'], i['mp'], i['signature_count']) 
        for i in dctd['data']['attributes']['signatures_by_constituency'] ])
    return HttpResponse(sigs_by_const_s, content_type='text/csv')
