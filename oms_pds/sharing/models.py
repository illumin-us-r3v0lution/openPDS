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

from django.conf import settings
from django.db import models
from oms_pds.trust.models import Role, SharingLevel


class Tokens(models.Model):
    token_id = models.CharField(max_length=120)
    role = models.ManyToManyField(Role)  

class OverallSharingLevel(models.Model):
    level = models.IntegerField(default=0)

class ProbeGroupSetting(models.Model):
    name = models.CharField(max_length=120)
    issharing = models.BooleanField(default=False)
#    probes = ListField(ReferenceField(FunfResource))

#class Sharing(models.Model):
#    overallsharinglevel = models.ForeignKey(SharingLevel)
#    roles = models.ManyToManyField(Role) #a list of roles the user is currently sharing with
#    probes = models.ManyToManyField(ProbeGroupSetting)#a list of probes the user is currently sharing 

#class Space(Document):
#    """ @name : The user defined name of the role
#        @purpose : A list of purposes associated with this role
#        @tokens : A list of oauth tokens of users assigned to this role """
#    name = StringField(max_length=120, required=True)
#    purpose = ReferenceField(Purpose)
#
#class Time(Document):
#    level = IntField(required=True)
#    purpose = ReferenceField(Purpose)

