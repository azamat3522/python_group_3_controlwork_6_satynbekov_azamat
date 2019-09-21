from django.shortcuts import render
from

def index_view(request):
    products = Quest_book.objects.filter(balance__gt=0).order_by('name', 'category')
    return render(request, 'index.html', context={
        'products': products
    })
