from django.contrib import admin
from rest_framework import routers
from api.views import PollsViewSet, UserViewSet
from django.urls import path, include

from polls.apps import PollsConfig

router = routers.DefaultRouter()

for service in [
	PollsConfig
	]:
	for widget in service.widgets:
		router.register(widget["api"]["api_route"], widget["api"]["ViewSet"])
router.register('users', UserViewSet,)


urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]