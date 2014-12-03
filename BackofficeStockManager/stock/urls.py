from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from stock import api

urlpatterns = patterns('',
    url(r'^$', 'stock.views.stock_index', name='stock_index'),
    url(r'^newproduct$', 'stock.views.newproduct', name='newproduct'),
    url(r'^upgrade/(?P<id>\d+)$', 'stock.views.upgrade',{},name='upgrade'),
 	#API LINKS
    url(r'^api/$', api.StockList.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'xml'])