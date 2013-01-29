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

from django import forms
from oms_pds.trust.models import Scope, Role, SharingLevel
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple


scopeview = {}
for s in Scope.objects.all():
    scopeview.update({s.name:s.name})

roleview = {}
for r in Role.objects.all():
    roleview.update({r.name:r.name})

sharingview = {}
for sl in SharingLevel.objects.all():
    sharingview.update({sl.level:sl.level})

class PermissionsForm(forms.Form):
    groups = forms.MultipleChoiceField(roleview.viewitems(), widget=forms.CheckboxSelectMultiple)
    sensors = forms.MultipleChoiceField()
    sharinglevel = forms.MultipleChoiceField(sharingview.viewitems(), widget=forms.CheckboxSelectMultiple, label= "Sharing Level")

class Purpose_Form(forms.Form):
    purpose = forms.CharField(max_length=100)
    scopes = forms.MultipleChoiceField(scopeview.viewitems(), widget=forms.CheckboxSelectMultiple)
    roles = forms.MultipleChoiceField(roleview.viewitems(), widget=forms.CheckboxSelectMultiple)
    sharinglevels = forms.MultipleChoiceField(sharingview.viewitems(), widget=forms.CheckboxSelectMultiple, label= "Sharing Levels")
