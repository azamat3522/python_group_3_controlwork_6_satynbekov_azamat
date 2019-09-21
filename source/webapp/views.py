from django.shortcuts import render

from webapp.models import QuestBook


def index_view(request):
    books = QuestBook.objects.filter(status__startswith='active').order_by('create_time').reverse()
    # books = QuestBook.objects.all()
    return render(request, 'index.html', context={
        'books': books
    })
