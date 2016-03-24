from django.conf.urls import url, include
from diary.views import main

urlpatterns = [
    url(r'^$', main),
]