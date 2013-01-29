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

import re
from pymongo import Connection

from django.utils.text import compress_string
from django.utils.cache import patch_vary_headers

from django import http
#import settings
from django.conf import settings
import oms_pds.tastypie_mongodb.resources

class ExtractUser(object):
    """
        This middleware allows multiple pds instances to run on one OMS-PDS service.  It checks the incoming HTTP header request for 'multiPDS_user', if it exists, we create a seperated mongodb instance for the specified user.

	WARNING: The modification of django.conf settings is atypical and used with care.
         
    """
    def process_request(self, request):
        if 'multiPDS_user' in request.GET:
            print "setting multipds"
##	    db = Connection(
#	        host=getattr(settings, "MONGODB_HOST", None),
#	        port=getattr(settings, "MONGODB_PORT", None)
#	    )["User_"+request.GET['multiPDS_user']]
#	    oms_pds.tastypie_mongodb.resources.Connection = Connection(
#                host=getattr(settings, "MONGODB_HOST", None),
#                port=getattr(settings, "MONGODB_PORT", None)
#            )	["User_"+request.GET['multiPDS_user']]
            settings.MONGODB_DATABASE_MULTIPDS = "User_"+request.GET['multiPDS_user']
        else:
            settings.MONGODB_DATABASE_MULTIPDS = None

        return None

