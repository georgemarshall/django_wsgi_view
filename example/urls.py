from __future__ import absolute_import

from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from ladon.server.wsgi import LadonWSGIApplication
from twod.wsgi import make_wsgi_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from .wsgi import application as wsgi_application

service_modules = ['webservice']

ladon_application = LadonWSGIApplication(service_modules, [settings.BASE], client_root_path='/api/rpc')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^example/', include('example.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^api/rpc(/.*)$', make_wsgi_view(ladon_application)),
    url(r'^wsgi(/.*)$', make_wsgi_view(wsgi_application)),
)

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
