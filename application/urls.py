from django.conf.urls import patterns, url

urlpatterns = patterns('application.views',
    url(r'^home/$', 'home'),
    url(r'^hello/$', 'hello'),
)