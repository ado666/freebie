from django.conf.urls import patterns, include, url

from index import views
from fcompany import views as company_views
from foffer import views as offer_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'freebie.views.home', name='home'),
    # url(r'^freebie/', include('freebie.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index), # index / main or login
    url(r'login', views.login),
    url(r'logout', views.logout),

    url(r'company/getall', company_views.getall),
    url(r'company/get', company_views.get),
    url(r'company/save', company_views.save),

    url(r'offer/all', offer_views.all),
    url(r'offer/save', offer_views.save),
    url(r'offer/getbycompany', offer_views.getbycompany),
    url(r'offer/get', offer_views.get),
    url(r'offer/delete', offer_views.delete),
)
