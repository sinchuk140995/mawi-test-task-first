from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/electrocardiogram/(?P<id>[\d\w]+)/$', consumers.ElectrocardiogramConsumer),
]
