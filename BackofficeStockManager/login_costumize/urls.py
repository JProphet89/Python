from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'login_costumize.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^stock/', include('stock.urls', namespace='accounts')),

    url(r'^admin/', include(admin.site.urls)),
)
