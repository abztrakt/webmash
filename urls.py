from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('webmash.views',
    url(r'^objects/$', 'all_objects'),
    url(r'^$', 'index'),
)
