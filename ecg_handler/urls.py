from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(r'^electrocardiograms/$',
        views.ElectrocardiogramCreateView.as_view(),
        name='electrocardiogram-create'),
    url(r'^signals/$',
        views.SignalCreateView.as_view(),
        name='signal-create'),
    url(r'^electrocardiograms/status/$',
        TemplateView.as_view(template_name='ecg_handler/electrocardiogram.html'),
        name='signal-status'),
]
