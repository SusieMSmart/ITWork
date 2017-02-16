from __future__ import unicode_literals
from django.contrib.auth.models import User

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
		if self.views <0:
			self.views=0
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
	#last_visit =  models.DateTimeField()
	#first_visit = models.DateTimeField()
	
	def __unicode__(self):
		return self.title

		
class UserProfile(models.Model):
# This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)
	# The additional attributes we wish to include.
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	# Override the __unicode__() method to return out something meaningful!
	# Remember if you use Python 2.7.x, define __unicode__ too!
	def __str__(self):
		return self.user.username
