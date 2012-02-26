from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^mixer/', include('mixer.urls')),
) 
