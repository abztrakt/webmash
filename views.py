from django.shortcuts import render_to_response
from webmash.models import *

installed_types = ['Page', 'Folder', 'LocalText',]

def index(request):
    """ Renders the index page.
    """
    return render_to_response('index.html')

def all_objects(request):
    """ Renders a list of all objects in the system.
    """
    all = Base.objects.all()
    return render_to_response('all_objects.html', {'all':all,})

def object(request, object_slug):
    """ Renders any generic object.
    """
    object = Base.objects.get(slug=object_slug)
    return render_to_response('object.html', {'object':object,})

def containers(request):
    """ Renders a list of alli container type objects.
    """
    containers = Container.objects.all()
    return render_to_response('all_objects.html', {'all':containers,})

def container(request, object_slug):
    """ Renders any generic object.
    """
    object = Base.objects.get(slug=object_slug)
    return render_to_response('container.html', {'object':object,})

def artifacts(request):
    """ Renders a list of all artifact type objects.
    """
    artifacts = Artifact.objects.all()
    return render_to_response('all_objects.html', {'all':artifacts,})

def page(request):
    """ Render a page with all of it's child objects.
    """
    page = Page.objects.get(slug=object_slug)
    return render_to_response('page.html', {'object':object,})
