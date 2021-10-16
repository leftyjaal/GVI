from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from apps.test import test
import json

# Create your views here.
# def apiView(request):
# return HttpResponse('URL API')

class ApiView(View):
    
    @method_decorator(csrf_exempt)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        #jd = json.load(request.body)
        print(request.body)
        test()
        datos = {'holi' : "siiiuuu"}
        return JsonResponse(datos)
