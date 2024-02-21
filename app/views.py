from django.shortcuts import render, HttpResponse

# Create your views here.



def test(request):
    return HttpResponse("Hello World, Welcome to my chat app!")
