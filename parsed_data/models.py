# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class NaverData(models.Model):
	title = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	imgLink = models.URLField()
	urlLink = models.URLField()

	def __str__(self):
		return self.title.encode('utf-8')

	def dic(self):
		fields = ['title', 'price', 'imgLink', 'urlLink']
		result = {}
		for field in fields :
			result[field] = self.__dict__[field]
		return result