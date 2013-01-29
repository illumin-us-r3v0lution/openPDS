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

from bson import ObjectId
from pymongo import Connection

from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.conf import settings

from tastypie.bundle import Bundle
from tastypie.resources import Resource
import pdb

from oms_pds.pds.models import Profile

"""the MONGODB_DATABASE_MULTIPDS setting is set by extract-user-middleware in cases where we need multiple PDS instances within one PDS service """


db = Connection(
    host=getattr(settings, "MONGODB_HOST", None),
    port=getattr(settings, "MONGODB_PORT", None)
)
#[settings.MONGODB_DATABASE]


class Document(dict):
    # dictionary-like object for mongodb documents.
    __getattr__ = dict.get

class MongoDBResource(Resource):
    """
    A base resource that allows to make CRUD operations for mongodb.
    """
    def get_collection(self, request):
        """
        Encapsulates collection name.
        """
        try:
            # If no owner is specified in the request, we use the default from settings for now
            # moving forward, we'll want to remove this fallback and require that the owner is specified
            # from the owner uuid, we're looking up the internal identifier from the corresponding profile
            #pdb.set_trace()
            database = settings.MONGODB_DATABASE
            if (request and "datastore_owner__uuid" in request.GET):
                profile, created = Profile.objects.get_or_create(uuid = request.GET["datastore_owner__uuid"])
                database = "User_" + str(profile.id)
            
            print database
            return db[database][self._meta.collection]
        except AttributeError:
            raise ImproperlyConfigured("Define a collection in your resource.")

    def obj_get_list(self, request=None, **kwargs):
        """
        Maps mongodb documents to Document class.
        """
        return map(Document, self.get_collection(request).find())

    def obj_get(self, request=None, **kwargs):
        """
        Returns mongodb document from provided id.
        """
        return Document(self.get_collection(request).find_one({
            "_id": ObjectId(kwargs.get("pk"))
        }))

    def obj_create(self, bundle, request = None, **kwargs):
        """
        Creates mongodb document from POST data.
        """
        object_id = self.get_collection(request).insert(bundle.data)
        bundle.obj = self.obj_get(request, pk = object_id)
        return bundle

    def obj_update(self, bundle, request=None, **kwargs):
        """
        Updates mongodb document.
        """
        self.get_collection(request).update({
            "_id": ObjectId(kwargs.get("pk"))
        }, {
            "$set": bundle.data
        })
        return bundle

    def obj_delete(self, request=None, **kwargs):
        """
        Removes single document from collection
        """
        self.get_collection(request).remove({ "_id": ObjectId(kwargs.get("pk")) })

    def obj_delete_list(self, request=None, **kwargs):
        """
        Removes all documents from collection
        """
        self.get_collection(request).remove()

    def get_resource_uri(self, item):
        """
        Returns resource URI for bundle or object.
        """
        if isinstance(item, Bundle):
            pk = item.obj._id
        else:
            pk = item._id
        return reverse("api_dispatch_detail", kwargs={
            "resource_name": self._meta.resource_name,
            "api_name": self._meta.api_name, 
            "pk": pk
        })
