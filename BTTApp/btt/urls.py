from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'biker.views.index', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^biker/', include('biker.urls', namespace='bikers')),
    url(r'^admin/', include(admin.site.urls)),
)
