from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('form.html')
    return HttpResponse(template.render({}, request))

def authentication(request):
    username = request.POST['username']
    country = request.POST.getlist('country')[0]
    print(country)
    return redirect('room:index', username=username, room_name=country)
