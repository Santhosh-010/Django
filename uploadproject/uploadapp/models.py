from django.db import models

# Create your models here.
class Cricketer(models.Model):
	Name = models.CharField(max_length=50)
	cricketerimage = models.ImageField(upload_to= 'images/')


	class Meta:
		verbose_name = "Cricketer"
		verbose_name_plural = "Cricketers"


		def __str__(self):
			pass

