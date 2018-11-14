from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Polls(models.Model):
	numero_case = models.IntegerField()

	TOPIC_CHOICES = (
		("meteo", "Météo"),
		('news', 'Le Monde'),
		('youtube' , 'Youtube'),
		('gorafie' , 'Le gorafie'),
		)
	topics = models.CharField(
		max_length = 15,
		choices = TOPIC_CHOICES,
		default = '',
		help_text = ''
		)
	
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	username =  models.CharField(max_length = 55, default = "")

	def get(self, instance):
		return {
			"num" : self.numero_case,
			"topic" : self.topics,
			"id": instance.id,
		}

	def __str__(self):
		return "it's " + self.topics + " on case " + str(self.numero_case)
	class Meta:
        	verbose_name_plural = 'polls'