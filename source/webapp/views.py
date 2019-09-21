from django.shortcuts import render, redirect

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
