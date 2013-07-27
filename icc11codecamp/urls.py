from django.conf.urls import patterns, include, url
from website.views import IndexView, SessionsAPIListView, SessionsAPIRetrieveView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^api/sessions/$', SessionsAPIListView.as_view(), name='home'),
    url(r'^api/sessions/(?P<pk>\d+)/$', SessionsAPIRetrieveView.as_view(), name='home'),
)
