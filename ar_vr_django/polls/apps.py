from django.apps import AppConfig




from django.apps import AppConfig

from .form import PollsForm
from .models import Polls
from api.views import PollsViewSet
from api.serializers import PollsSerializer


class PollsConfig(AppConfig):
	name = 'polls'
	about = {
		"name": name,
		"widgets": [{
			"name": "Polls" ,
			"description": "Polls" ,
			"params": [
				{
					"name": "numero_case" ,
					"type": "int"
				},
				{
					"name": "topic" ,
					"type": "string"
				}
				],
				}]
		}

	widgets = [{
		"name": name,
		"template_name": "polls.html",
		"model": Polls,
		"form": PollsForm,
		"api": {
			"api_route": "polls",
			"api_url": "/api/polls",
			"ViewSet": PollsViewSet,
			"Serializer": PollsSerializer
		}
	}]