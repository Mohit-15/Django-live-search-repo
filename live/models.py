from django.db import models

# Create your models here.
class Service(models.Model):
	name = models.CharField(max_length = 40)
	description = models.CharField(max_length = 70)
	url = models.URLField(max_length=200)

	def __str__(self):
		return self.name
