from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pandatree.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'services.views.home', name='home'),
    url(r'^customers$', 'customers.views.customers', name='customers'),
    url(r'^contact$', 'customers.views.contact', name='contact'),
    url(r'^thanks$', 'customers.views.thanks', name='thanks'),
    url(r'^admin/', include(admin.site.urls)),
)
