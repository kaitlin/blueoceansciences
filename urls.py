from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
    url(r'^$', 'direct_to_template', { 'template':'index.html'}), 
    url(r'^about$', 'direct_to_template', { 'template':'about.html'}), 
    url(r'^projects$', 'direct_to_template', {'template':'projects.html'}), 
    url(r'^projects/bosme$', 'direct_to_template', {'template':'projects/bosme.html'}), 
    url(r'^projects/waves$', 'direct_to_template', {'template':'projects/waves.html'}), 
    url(r'^projects/bossa$', 'direct_to_template', {'template':'projects/bossa.html'}), 
    url(r'^projects/seed$', 'direct_to_template', {'template':'projects/seed.html'}), 
    url(r'^projects/coast$', 'direct_to_template', {'template':'projects/coast.html'}), 
    url(r'^projects/leafs$', 'direct_to_template', {'template':'projects/leafs.html'}), 
    url(r'^media$', 'direct_to_template', {'template': 'media.html'}), 
    url(r'^media/videos$', 'direct_to_template', {'template': 'media/videos.html'}), 
    url(r'^media/photos$', 'direct_to_template', {'template':'media/photos.html'}), 
    # Example:
    # (r'^blueoceansciences/', include('blueoceansciences.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

