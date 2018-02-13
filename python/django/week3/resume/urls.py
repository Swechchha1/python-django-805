#Resume url conf

from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'resume'

urlpatterns = [
    path('', views.home, name='home'),
     ]
