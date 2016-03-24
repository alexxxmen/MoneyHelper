from django.conf.urls import url, include
from forecast.views import main

urlpatterns = [
    url(r'^$', main),
]