from django.db import models

# Create your models here.
class Trainer_info(models.Model):
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	DOMAIN = models.CharField(max_length=50)
	EXPERIENCE = models.IntegerField()
	BRANCH = models.CharField(max_length=50)
	ADDRESS = models.CharField(max_length=50)
	GENDER = models.CharField(max_length=50)
	SALARY = models.FloatField()

	class Meta:
		verbose_name = "Trainer_info"
		verbose_name_plural = "Trainer_infos"

		def __str__(self):
			pass

