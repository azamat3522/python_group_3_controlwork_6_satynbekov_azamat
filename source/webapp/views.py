from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import QuestBookForm
from webapp.models import QuestBook, STATUS_CHOICES


def index_view(request):
    books = QuestBook.objects.filter(status__startswith='active').order_by('create_time').reverse()
    # books = QuestBook.objects.all()
    return render(request, 'index.html', context={
        'books': books
    })

def book_create_view(request):
    if request.method == 'GET':
        form = QuestBookForm()
        return render(request, 'create.html', context={
            'status_choices': STATUS_CHOICES,
            'form': form
        })
    elif request.method == 'POST':
        form = QuestBookForm(data=request.POST)
        if form.is_valid():
            QuestBook.objects.create(
                author_name=form.cleaned_data['name'],
                author_mail=form.cleaned_data['mail'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def book_update_view(request, pk):
    book = get_object_or_404(QuestBook, pk=pk)
    if request.method == 'GET':
        form = QuestBookForm(data={
            'name': book.author_name,
            'mail': book.author_mail,
            'text': book.text
        })
        return render(request, 'update.html', context={'form': form, 'book': book})

    elif request.method == 'POST':
        form = QuestBookForm(data=request.POST)
        if form.is_valid():
            book.author_name = form.cleaned_data['name']
            book.author_mail = form.cleaned_data['mail']
            book.text = form.cleaned_data['text']
            book.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'book': book})

def book_delete_view(request, pk):
    book = get_object_or_404(QuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={
            'book': book
        })

    elif request.method == 'POST':
        book.delete()
        return redirect('index')
