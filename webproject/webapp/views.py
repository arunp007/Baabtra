from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.

def web(request):
    return render(request, 'website.html')
