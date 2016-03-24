from django.shortcuts import render
from notebook.models import Category


def main(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {'categories': categories})
