from django.urls import path, include 

from .views import ApiView

urlpatterns = [
    path('post/', ApiView.as_view(), name='post_list'),
]