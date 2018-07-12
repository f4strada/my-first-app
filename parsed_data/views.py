# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def jsonExport(request, tag=None):
	entries = NaverData.objects.get( tag=int(tag) );
	data = entries.dic()
	return HttpResponse( json.dumps(data), content_type="application/json" )