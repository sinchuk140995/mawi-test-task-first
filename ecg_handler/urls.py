from django.conf.urls import url

from ecg_handler import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name='home'),
]
