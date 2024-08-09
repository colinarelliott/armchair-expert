from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('upload/', views.upload, name='upload'),
    path('send_chat/', views.send, name='send_chat'),
]