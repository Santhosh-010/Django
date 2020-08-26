from django.db import models

# Create your models here.
class Batsmen_Info(models.Model):
	First_Name = models.CharField(max_length=50)
	Last_Name = models.CharField(max_length=50)
	Country = models.CharField(max_length=50)
	Age = models.IntegerField()
	Runs = models.IntegerField()
	Avg = models.FloatField()
	Rank = models.IntegerField()
	Played = models.IntegerField()
	Strike_rate = models.FloatField()

	class Meta:
		verbose_name = "Batsmen_Info"
		verbose_name_plural = "Batsmen_Infos"


		def __str__(self):
			pass

