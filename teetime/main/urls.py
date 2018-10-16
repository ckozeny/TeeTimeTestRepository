from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('membership', views.membership, name='membership'),
    path('scheduling', views.scheduling, name='scheduling'),
    path('events', views.events, name='events'),
    path('contact', views.contact, name='contact'),
]
