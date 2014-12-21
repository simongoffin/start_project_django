from django.conf.urls import patterns, url

urlpatterns = patterns('load.views',
    url(r'^home/$', 'home'),
)