from django.db import models

# Create your models here.
class student_details(models.Model):
	FIRST_NAME = models.CharField(max_length=50)
	LAST_NAME = models.CharField(max_length=50)
	USN = models.CharField(max_length=50)
	AGE = models.IntegerField()
	EMAIL = models.EmailField()
	GENDER = models.CharField(max_length=50)
	DOB = models.DateField()
	

	class Meta:
		verbose_name = "student_details"
		verbose_name_plural = "student_detailss"

		def __str__(self):
			return self.FIRST_NAME

