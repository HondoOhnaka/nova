from django.conf.urls.defaults import patterns, include, url
from nova.views import index_action

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'img',
    }),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'js',
    }),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'css',
    }),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': 'images',
    }),
    
    (r'^admin/', include(admin.site.urls)),
    
    # catch all
    #(r'', index_action),

    
)
