from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from .validate import validate_file_extension, validate_file_extension_image



# Create your models here.

class Addbook(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique = True)
	

	AVAILABLE_CATEGORY = (
		('SOFTWARE', 'Software_books'), 
		('HARDWARE', 'Hardware_books'), 
		('NETWORKING', 'Networking_books'), 
		('PROGRAMMING', 'programming_books'),
		('LECTURE_NOTES', 'lecture_notes'),
		('OTHERS', 'others'),
		)


	category = models.CharField(max_length=50 ,choices=AVAILABLE_CATEGORY)
	description = models.TextField()
	date= models.DateField(auto_now_add=True, auto_now=False)
	author = models.CharField(max_length=50)
	book = models.FileField(validators=[validate_file_extension])
	book_cover = models.ImageField()
	
		

	def __unicode__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("bookstore:software", kwargs={"id": self.id})

class Add_lecture_note(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=200)
	description = models.TextField()
	date_note = models.DateField(auto_now_add=True, auto_now=False)
	level = models.SmallIntegerField()
	book_note = models.FileField()
	book_cover_note = models.FileField()


	def __unicode__(self):
		return self.title


