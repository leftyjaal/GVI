from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rendererView(request):
    return HttpResponse('URL renderer')