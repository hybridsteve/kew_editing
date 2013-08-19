from django.db import models
import datetime
from django.utils import timezone

# this model represents a type of project. types are used to organize and display the projects.
class ProjectType(models.Model):
	type = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.type

# this model represents a completed bit of work.
class Project(models.Model):
	type = models.ForeignKey(ProjectType)
	#author = models.CharField(max_length = 200)
	title = models.CharField(max_length = 300)
	#publisher = models.CharField(max_length = 300)
	pub_date = models.DateTimeField('date added')
	complete_citation = models.CharField(max_length = 500)

	def __unicode__(self):
		return self.title

# this model represents images in the image rotation.
class ProjectImage(models.Model):
	project = models.ForeignKey(Project) #this might not be useful for anything
	image_url = models.CharField(max_length = 200)
	description = models.CharField(max_length = 300)
	display = models.BooleanField(default = False)

	def __unicode__(self):
		return self.image_url
