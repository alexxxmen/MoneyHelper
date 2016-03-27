from django.conf.urls import url
from notebook import views

urlpatterns = [
    url(r'^$', views.main),
    url(r'^add/$', views.add_note),
    url(r'^(?P<note_id>\d+)/$', views.get_note),
    url(r'^(?P<note_id>\d+)/delete/$', views.note_delete),
    url(r'^(?P<note_id>\d+)/edit/$', views.note_edit),
    url(r'^category/$', views.get_categories),
    url(r'^category/add/$', views.category_add),
    url(r'^category/(?P<category_id>\d+)/$', views.get_category),
    url(r'^category/(?P<category_id>\d+)/delete/$', views.category_delete),
    url(r'^category/(?P<category_id>\d+)/edit/$', views.category_edit),
]
