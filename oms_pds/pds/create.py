from oms_pds.pds.models import Profile
from django.http import HttpResponse
import json

def init(request):
    p = Profile(uuid = request.GET.get('datastore_owner__uuid'))
    response_dict = {}
    response_dict['status'] = "success"

    return HttpResponse(json.dumps(response_dict), content_type='application/json') 
