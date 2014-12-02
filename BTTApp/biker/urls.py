from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from biker import api

urlpatterns = patterns('',
    url(r'^$', 'biker.views.index', name='stock_index'),
    url(r'^newbiker$', 'biker.views.newbiker', name='newbiker'),
    url(r'^(?P<id>\d+)$', 'biker.views.bikerview',{},name='bikerview'),

    #API LINKS
    url(r'^api/$', api.BikerList.as_view()),
    url(r'^api/set$', api.BikerSetInfo.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'xml'])