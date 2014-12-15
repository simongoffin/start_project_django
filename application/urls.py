from django.conf.urls import patterns, url

urlpatterns = patterns('application.views',
    url(r'^home/$', 'home'),
    url(r'^hello/$', 'hello'),
    url(r'^confirmation/$', 'confirmation'),
    url(r'^message/$', 'message'),
)