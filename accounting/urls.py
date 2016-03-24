from django.conf.urls import url, include
from accounting.views import main

urlpatterns = [
    url(r'^$', main),
]