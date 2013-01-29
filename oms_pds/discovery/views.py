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

from django.http import HttpResponse
import json
from django.template import RequestContext
from django.shortcuts import render_to_response
from oms_pds.settings import SERVER_OMS_REGISTRY
from oms_pds.trust.models import Role
from django import forms
import json
import requests

def ping(request):
    response = {"success":True}
    return HttpResponse(json.dumps(response), mimetype="application/json")


def members(request):
    roles = Role.objects.all()
    r = requests.get("http://"+SERVER_OMS_REGISTRY+"/discovery/members")
    print r
    template = {}
    template['profiles'] = r.json['profiles']
    template['roles'] = roles
    print template
    return render_to_response('discovery/members.html',
        template,
        RequestContext(request))



