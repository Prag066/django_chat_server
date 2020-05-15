from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Message

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    userData = Profile.objects.all()
    messageData = Message.objects.all()
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'userData':userData,
        'messageData':messageData
    })



