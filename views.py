from django.shortcuts import render_to_response
from webmash.models import *

def index(request):
    return render_to_response('index.html')

def all_objects(request):
    all = Base.objects.all()
    return render_to_response('all_objects.html', {'all':all,})
