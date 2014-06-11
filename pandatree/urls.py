from django.conf.urls import patterns, include, url
from blog import views
from django.conf.urls.static import static

from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pandatree.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'services.views.home', name='home'),
    url(r'^services$', 'services.views.services', name='services'),
    url(r'^customers$', 'customers.views.customers', name='customers'),
    url(r'^contact$', 'customers.views.contact', name='contact'),
    url(r'^thanks$', 'customers.views.thanks', name='thanks'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', views.IndexView.as_view(), name='blog'),
     url(r'(?P<slug>[^/]+)/$', views.PostView.as_view(), name='post'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT


   
      


)
