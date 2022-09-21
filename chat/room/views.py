from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def index(request, username, room_name):
    template = loader.get_template('room.html')
    username = request.GET.get('username')
    return HttpResponse(template.render({'username': username, 'room_name': room_name}, request))

def room(request, room_name):
    template = loader.get_template('room.html')
    return HttpResponse(template.render({'room_name': room_name}, request))

