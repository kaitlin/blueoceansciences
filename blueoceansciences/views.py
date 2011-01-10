from django.shortcuts import render_to_response
from django.conf import settings

def index(request):
    return render_to_response('index.html')

def about(request):
    return render_to_response('about.html')

def projects(request):
    return render_to_response('projects.html')

def media(request):
    return render_to_response('media.html')
