from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
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

        id=json.loads(request.body)["id"]
        name=json.loads(request.body)["name"]
        email=json.loads(request.body)["email"]
        position=json.loads(request.body)["position"]
        music=json.loads(request.body)["music"]
        
        send_mail(
            f"Tu video generado en GVI está listo",
            f"Hola {name} este es el enlace de descarga de tu video: https://gvi-videos.s3.us-east-2.amazonaws.com/{id}/{id}.mp4 \nGracias por utilizar GVI",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
            )

        return JsonResponse(json.loads(request.body))
