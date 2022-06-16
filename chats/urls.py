from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.homepage, name='home'),
    path('index', views.index, name='chathome'),
    path('options',views.options,name='options'),
    path('appointment',views.appointment,name='appointment'),
    path('<str:username>/', views.chatPage, name='chat'),
]
