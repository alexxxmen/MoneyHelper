from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^notebook/', include('notebook.urls')),
    url(r'^admin/', admin.site.urls),
]
