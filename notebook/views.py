from django.shortcuts import render, redirect, get_object_or_404, Http404
from notebook.models import Note, Category
from MoneyHelper import CONST
from django.core.exceptions import ObjectDoesNotExist


def main(request):
    notes = Note.objects.all()
    categories = Category.objects.all()
    return render(request, "index_notebook.html", {"notes": notes,
                                                   "categories": categories,
                                                   })


def add_note(request):
    pass


def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete() if note else None
    return redirect('/notebook/')


def note_edit(request, note_id):
    pass


def get_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    categories = Category.objects.all()
    context = {
        "note": note,
        "categories": categories,
        "title": note.title[0:10]+'...'
    }
    return render(request, 'notebook_note.html', context)


def get_notes(request, category_id):
    """
    Return template with notes filtered by category_id
    """
    notes = Note.objects.filter(category=category_id)
    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    context = {
        "notes": notes,
        "categories": categories,
        "title": category.title + " : " + CONST.PROJECT_NAME
    }
    return render(request, 'notebook_notes_cat.html', context)




def get_category(request, category_id):
    """
    *Возможно не понадобится.
    """
    pass


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'notebook_categories.html')


def category_add(request):
    pass


def category_delete(request, category_id):
    pass


def category_edit(request, category_id):
    pass
