from django.urls import path, include 

from apps.renderer.views import rendererView

urlpatterns = [
    path('renderApp/', rendererView),
    
]
