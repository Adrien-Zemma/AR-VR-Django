from django.forms import ModelForm, TextInput

from .models import Polls

class PollsForm(ModelForm):
	class Meta:
		model = Polls
		exclude = ['user']
		