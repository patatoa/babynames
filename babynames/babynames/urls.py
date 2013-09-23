from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'babynames.views.home', name='home'),
    # url(r'^babynames/', include('babynames.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'babynames_app.views.main', name='main'),
    url(r'^like/(?P<name_id>\d+)/$', 'babynames_app.views.like'),
    url(r'^vote_down/(?P<name_id>\d+)/$', 'babynames_app.views.vote_down'),
    url(r'^info/(?P<name_id>\d+)/$', 'babynames_app.views.info')
)
