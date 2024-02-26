
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name='home'),

    path('details/<str:pk>/', views.details, name='details'),

    path('sent_msg/<str:pk>/', views.sentMessage, name='sent_msg'),

]
