from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('webmash.views',
    url(r'^page/(?P<object_slug>\w+)', 'object'),
    url(r'^object/(?P<object_slug>\w+)', 'object'),
    url(r'^objects/$', 'all_objects'),
    url(r'^container/(?P<object_slug>\w+)', 'container'),
    url(r'^containers/$', 'containers'),
    url(r'^artifacts/$', 'artifacts'),
    url(r'^$', 'index'),
)
