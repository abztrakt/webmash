from django import http
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
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
    """ Renders a list of all container type objects.
    """
    containers = Container.objects.all()
    return render_to_response('all_objects.html', {'all':containers,})

def folder(request, folder_slug):
    """ Renders a list of all child items in the folder.
    """
    folder = Folder.objects.get(slug=folder_slug)
    children = folder.related_items.values()
    return render_to_response('folder.html', {'children':children})

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
        children.append(Base.objects.get(id=a['id']).downcast())
    return render_to_response('superpage.html', {'page':page, 'children':children,})

def page_to_pdf(request, page_slug):
    """ Render a page with all of it's child objects.
    """
    page = Page.objects.get(slug=page_slug)
    children = []
    child_artifacts = page.related_items.values()
    for a in child_artifacts:
        children.append(Base.objects.get(id=a['id']).downcast())

    template = get_template('superpage.html')
    context = Context({'page': page, 'children':children,})
    html = template.render(context)
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), mimetype='application/pdf')
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))
