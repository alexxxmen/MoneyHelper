from django.conf.urls import url, include
from django.contrib import admin
from MoneyHelper import views


urlpatterns = [
    url(r'^$', views.main),
    url(r'^admin/', admin.site.urls),
    url(r'^calendar/', include('diary.urls')),
    url(r'^notebook/', include('notebook.urls')),
]
