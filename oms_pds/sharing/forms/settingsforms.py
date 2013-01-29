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
from oms_pds.sharing.models import Tokens, OverallSharingLevel, ProbeGroupSetting
from oms_pds.pds.models import SharingLevel, Role, Profile
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple


#tokenview = {}
#for t in Tokens.objects.all():
#    tokenview.update({t.id:t.role.name})

oslview = {}
pgsview = {}
slview = {}
rview = {}


class Sharing_Form(forms.Form):
    #tokens = forms.MultipleChoiceField(tokenview.viewitems(), widget=forms.CheckboxSelectMultiple)
    probes = forms.MultipleChoiceField(pgsview.viewitems(), widget=forms.CheckboxSelectMultiple)
    roles = forms.MultipleChoiceField(rview.viewitems(), widget=forms.CheckboxSelectMultiple)
    sharinglevel = forms.MultipleChoiceField(slview.viewitems(), widget=forms.RadioSelect, label= "Overall Sharing Level")
    def update_form(self, uuid):
        new_pgsview = {}
        new_slview = {}
        new_rview = {}
	p = Profile.objects.get(uuid=uuid)
        for pgs in ProbeGroupSetting.objects.all():#(datastore_owner_id=uuid):
            new_pgsview.update({pgs.name:pgs.name})
        
        for sl in p.sharinglevel_owner.all():
            new_slview.update({sl.level:sl.level})
        
        for r in p.role_owner.all():
            new_rview.update({r.name:r.name})

	self.fields['roles'] = forms.MultipleChoiceField(new_rview.viewitems(), widget=forms.CheckboxSelectMultiple)
	self.fields['probes'] = forms.MultipleChoiceField(new_pgsview.viewitems(), widget=forms.CheckboxSelectMultiple)
	self.fields['sharinglevel'] = forms.MultipleChoiceField(new_slview.viewitems(), widget=forms.RadioSelect, label= "Overall Sharing Level")
#    probes = None
#    roles = None
#    sharinglevel = None
    
#        self.probes = forms.MultipleChoiceField(pgsview.viewitems(), widget=forms.CheckboxSelectMultiple)
#        self.roles = forms.MultipleChoiceField(rview.viewitems(), widget=forms.CheckboxSelectMultiple)
#        self.sharinglevel = forms.MultipleChoiceField(slview.viewitems(), widget=forms.RadioSelect, label= "Overall Sharing Level")

class CreateSharingForm(forms.Form):

    probes = forms.MultipleChoiceField(pgsview.viewitems(), widget=forms.CheckboxSelectMultiple)
    roles = forms.MultipleChoiceField(rview.viewitems(), widget=forms.CheckboxSelectMultiple)
    sharinglevel = forms.MultipleChoiceField(slview.viewitems(), widget=forms.RadioSelect, label= "Overall Sharing Level")

    @property
    def helper(self):
        form = CreateSharingForm()
        helper = FormHelper()
        reset = Reset('','Reset')
        helper.add_input(reset)
        submit = Submit('','Submit')
        helper.add_input(submit)
        helper.form_action = '/sharing/update'
        helper.form_method = 'POST'
        return helper

