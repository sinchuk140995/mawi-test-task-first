from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^electrocardiograms/$',
        views.ElectrocardiogramCreateView.as_view(),
        name='electrocardiogram-create'),
    url(r'^signals/$',
        views.SignalCreateView.as_view(),
        name='signal-create'),
]
