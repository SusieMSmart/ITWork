from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Category(models.Model):
	cmax = 128
	name = models.CharField(max_length=cmax, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	
	class Meta:
		verbose_name_plural = 'Categories'
	
	def __unicode__(self):
		return self.name
	
	
class Page(models.Model):
	pmax = 128
	umax = 200
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=pmax)
	url = models.URLField(max_length=umax)
	views = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title
		
from rango.models import Category

