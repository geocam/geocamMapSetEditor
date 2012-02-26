from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('mixer.views',
    url(r'^$', 'index'),
)
