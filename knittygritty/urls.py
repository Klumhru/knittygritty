from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.admindocs import urls as admin_urls
from base import views as base_views
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'knittygritty.views.home', name='home'),
    url(r'^$', base_views.Home.as_view(), name='home'),
    # url(r'^knittygritty/', include('knittygritty.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include(admin_urls)),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
