from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('webmash.views',
    url(r'^object/(?P<object_slug>\w+)', 'object'),
    url(r'^objects/$', 'all_objects'),
    url(r'^$', 'index'),
)
