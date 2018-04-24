from django.shortcuts import render
from .models import Comic

# Create your views here.
def comic_list(request):
    return render(request, 'shop/comic_list.html', {})