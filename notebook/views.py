from django.shortcuts import render, redirect, get_object_or_404
from notebook.models import Note, Category


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
    note.delete()
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


def get_category(request, category_id):
    pass


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'notebook_category.html')


def category_add(request):
    pass


def category_delete(request, category_id):
    pass


def category_edit(request, category_id):
    pass
