from django.contrib import admin
from notebook.models import Note, Category


admin.site.register(Note)
admin.site.register(Category)
