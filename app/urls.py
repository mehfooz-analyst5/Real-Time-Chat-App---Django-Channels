
from django.urls import path, include
from . import views


urlpatterns = [

    path('', views.index, name='home'),

    path('details/<int:pk>/', views.details, name='details')

]
