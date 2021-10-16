from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def modelView(request):
    return HttpResponse('URL model')