from tastypie.authentication import Authentication
import httplib
import settings
import json
import pdb
import requests

class OAuth2Authentication(Authentication):

    def get_userinfo_from_token(self, token, scope):
        # upon success, will return a json {'key':'value'}
        userinfo = {}
        try:
	    r = requests.get("http://"+settings.SERVER_OMS_REGISTRY+"/get_key_from_token?bearer_token="+str(token))
            if r.json['status'] == 'error':
                raise Exception(result['error'])

        except Exception as ex:
            print ex
            return False
            print "successfully got key: returning"
        return r.json

    def __init__(self, scope):
        self.scope = scope

    def is_authenticated(self, request, **kwargs):
        token = request.GET['bearer_token'];
        print token
        print self.scope
	
#       key = self.__get_userinfo_from_token(token, self.scope)
#	print "-----key-----"
#	print key	
	
#	settings.MONGODB_DATABASE = "User_"+str(key)
	
        return True

    def get_identifier(self, request):
        return request.GET.get('datastore_owner')


