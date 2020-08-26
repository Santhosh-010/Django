from django.db import models

# Create your models here.
class AccDetails(models.Model):
	FirstName = models.CharField(max_length=50)
	LastName = models.CharField(max_length=50)
	DOB = models.DateField()
	Address = models.CharField(max_length=50)
	AccType = models.CharField(max_length=50)
	PanNo = models.CharField(max_length=50)

	class Meta:
		verbose_name = "AccDetails"
		verbose_name_plural = "AccDetailss"

		def __str__(self):
			pass
    