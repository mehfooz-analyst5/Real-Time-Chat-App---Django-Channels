import json
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from .models import Profile, Friend, ChatMessage
from .forms import ChatMessageForm
from django.http import JsonResponse




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
    user  = request.user.profile
    print('user : ', user)
    profile = Profile.objects.get(id=friend.profile.id)
    print('profile : ', profile)
    chats = ChatMessage.objects.all()

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.msg_sender = user
            message.msg_receiver = profile
            message.save()
            print('Message sent : ',  message.message)
            return redirect('details', pk=friend.profile.id)
            # form = ChatMessageForm()
    else:
        form = ChatMessageForm()

    context = {
        'friend': friend,
        'form': form,
        'chats': chats,
        'user': user,
        'profile': profile
    }
    return render(request, 'app/details.html', context)



def sentMessage(request, pk):
    user  = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    new_chat = data['msg']

    new_chat_messages = ChatMessage.objects.create(
        message=new_chat,
        msg_sender=user,
        msg_receiver=profile,
        seen = False
    )

    print('new_chat : ', new_chat)

    return JsonResponse(new_chat_messages.message, safe=False)




def receiveMessage(request, pk):
    user  = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)