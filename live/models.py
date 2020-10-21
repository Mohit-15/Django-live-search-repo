from django.db import models
from io import BytesIO
from django.core.files import File

# Create your models here.
class Service(models.Model):
	name = models.CharField(max_length = 40)
	description = models.CharField(max_length = 70)
	url = models.URLField(max_length=200)
	image = models.ImageField(upload_to = "images", blank = True)

	def __str__(self):
		return self.name

	# def save(self, *args, **kwargs):
	# 	fname = f'thumbnail-{self.name}.jpg'
	# 	self.image.save(fname, File(BytesIO()), save = False)
	# 	super().save(*args, **kwargs)
