from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('webmash.views',
    url(r'^page/(?P<page_slug>.*)', 'page'),
    url(r'^pdf/(?P<page_slug>.*)', 'page_to_pdf'),
    url(r'^folder/(?P<folder_slug>.*)', 'folder'),
    url(r'^object/(?P<object_slug>.*)', 'object'),
    url(r'^objects/$', 'all_objects'),
    url(r'^containers/$', 'containers'),
    url(r'^artifacts/$', 'artifacts'),
    url(r'^$', 'index'),
)
