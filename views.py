from django.shortcuts import render_to_response
from webmash.models import *

installed_types = [Page, Folder, LocalText,]

def all_objects(request):
    """ Renders a list of all objects in the system.
    """
    all = Base.objects.all()
    return render_to_response('all_objects.html', {'all':all,})

def artifacts(request):
    """ Renders a list of all artifact type objects.
    """
    artifacts = Artifact.objects.all()
    return render_to_response('all_objects.html', {'all':artifacts,})

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

def index(request):
    """ Renders the index page.
    """
    return render_to_response('index.html')

def object(request, object_slug):
    """ Renders any generic object.
    """
    object = Base.objects.get(slug=object_slug)
    return render_to_response('object.html', {'object':object,})

def page(request, page_slug):
    """ Render a page with all of it's child objects.
    """
    page = Page.objects.get(slug=page_slug)
    children = []
    child_artifacts = page.related_items.values()
    for a in child_artifacts:
        for t in installed_types:
            try:
                children.append(t.objects.get(id=a['id']))
            except:
                pass # catch exceptions silently since only one of the installed types will find a match
    return render_to_response('page.html', {'page':page, 'children':children,})
