from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import Profile, Friend




# Create your views here.

def index(request):
    user = request.user.profile
    friends = user.friends.all()
    print(friends)

    context = {
        'user': user,
        'friends': friends
    }

    return render(request, 'app/index.html', context)


def details(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    print(friend)

    context = {
        'friend': friend
    }
    return render(request, 'app/details.html', context)
