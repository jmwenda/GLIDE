from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GLIDE.views.home', name='home'),
    # url(r'^GLIDE/', include('GLIDE.foo.urls')),
    (r'^glide/$', 'GLIDEAPP.views.index'),
    (r'^glide/(?P<glide_id>\d+)/$', 'GLIDEAPP.views.detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
