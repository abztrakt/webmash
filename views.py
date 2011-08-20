from django import http
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import cgi
from webmash.models import *
import urllib

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
    #TODO: get this pdfcss to read from a css file in the site
    pdfcss = """
* { background-color: none; }
html, address,
blockquote,
body, dd, div,
dl, dt, fieldset, form,
frame, frameset,
h1, h2, h3, h4,
h5, h6, noframes,
ol, p, ul, center,
dir, hr, menu, pre   { display: block; unicode-bidi: embed }
li              { display: block; margin: 1px; padding: 1px; }
head            { display: none }
table           { display: table }
tr              { display: table-row }
thead           { display: table-header-group }
tbody           { display: table-row-group }
tfoot           { display: table-footer-group }
col             { display: table-column }
colgroup        { display: table-column-group }
td, th          { display: table-cell }
caption         { display: table-caption }
th              { font-weight: bolder; text-align: center }
caption         { text-align: center }
body            { margin: 8px }
h1              { font-size: 2em; margin: .67em 0 }
h2              { font-size: 1.5em; margin: .75em 0 }
h3              { font-size: 1.17em; margin: .83em 0 }
h4, p,
blockquote, ul,
fieldset, form,
ol, dl, dir,
menu            { margin: 1.12em 0 }
h5              { font-size: .83em; margin: 1.5em 0 }
h6              { font-size: .75em; margin: 1.67em 0 }
h1, h2, h3, h4,
h5, h6, b,
strong          { font-weight: bolder }
blockquote      { margin-left: 40px; margin-right: 40px }
i, cite, em,
var, address    { font-style: italic }
pre, tt, code,
kbd, samp       { font-family: monospace }
pre             { white-space: pre }
button, textarea,
input, select   { display: inline-block }
big             { font-size: 1.17em }
small, sub, sup { font-size: .83em }
sub             { vertical-align: sub }
sup             { vertical-align: super }
table           { border-spacing: 2px; }
thead, tbody,
tfoot           { vertical-align: middle }
td, th, tr      { vertical-align: inherit }
s, strike, del  { text-decoration: line-through }
hr              { border: 1px inset }
ol, ul, dir,
menu, dd        { margin-left: 40px }
ol              { list-style-type: decimal }
ol ul, ul ol,
ul ul, ol ol    { margin-top: 0; margin-bottom: 0 }
ul li           { list-style-type: none; }
u, ins          { text-decoration: underline }
br:before       { content: "\A"; white-space: pre-line }
center          { text-align: center }
:link, :visited { text-decoration: underline }
:focus          { outline: thin dotted invert }

/* Begin bidirectionality settings (do not change) */
BDO[DIR="ltr"]  { direction: ltr; unicode-bidi: bidi-override }
BDO[DIR="rtl"]  { direction: rtl; unicode-bidi: bidi-override }

*[DIR="ltr"]    { direction: ltr; unicode-bidi: embed }
*[DIR="rtl"]    { direction: rtl; unicode-bidi: embed }
    """
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result, default_css=pdfcss)
    if not pdf.err:
        return http.HttpResponse(result.getvalue(), mimetype='application/pdf')
    return http.HttpResponse('We had some errors<pre>%s</pre>' % cgi.escape(html))
