from oms_pds.pds.models import Profile, SharingLevel, Purpose
from oms_pds.pds.api import SharingLevelResource, PurposeResource
from django.http import HttpResponse
import json


def validateRequest(request):
    if not request.GET.has_key('datastore_owner__uuid'):
        raise Exception('Missing datastore_owner__uuid.  Please add it as a querystring parameter.')
    return

def create(request):
    validateRequest(request)    
    p = Profile(uuid = request.GET.get('datastore_owner__uuid'))
    p.save()
    is_success = initializeTrustWrapper(p)
    print is_success
    response_dict = {}
    response_dict['status'] = "success"

    return HttpResponse(json.dumps(response_dict), content_type='application/json')

def initializeTrustWrapper(profile):

    p0 = Purpose(name="PDS", datastore_owner=profile)
    p0.save()
    print p0

    s0 = SharingLevel(level = 0, datastore_owner=profile, isselected = True)
    s1 = SharingLevel(level = 1, datastore_owner=profile, isselected = False)
    s2 = SharingLevel(level = 2, datastore_owner=profile, isselected = False)
    s3 = SharingLevel(level = 3, datastore_owner=profile, isselected = False)
    s0.save()
    s1.save()
    s2.save()
    s3.save()
    # Mapping each sharing level to the purpose PDS
    s0.purpose = [p0]
    s1.purpose = [p0]
    s2.purpose = [p0]
    s3.purpose = [p0]
    # we need to save the sharing levels twice, becuse the act of saving creates the primary key necessary to map sharing level to purpose
    s0.save()
    s1.save()
    s2.save()
    s3.save()
    

    return True


