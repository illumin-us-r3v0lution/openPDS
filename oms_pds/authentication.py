# Copyright (C) 2012 Massachusetts Institute of Technology and Institute 
# for Institutional Innovation by Data Driven Design Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE  MASSACHUSETTS INSTITUTE OF
# TECHNOLOGY AND THE INSTITUTE FOR INSTITUTIONAL INNOVATION BY DATA
# DRIVEN DESIGN INC. BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE 
# USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Except as contained in this notice, the names of the Massachusetts 
# Institute of Technology and the Institute for Institutional 
# Innovation by Data Driven Design Inc. shall not be used in 
# advertising or otherwise to promote the sale, use or other dealings
# in this Software without prior written authorization from the 
# Massachusetts Institute of Technology and the Institute for 
# Institutional Innovation by Data Driven Design Inc

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


