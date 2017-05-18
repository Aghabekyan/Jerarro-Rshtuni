from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +\
    patterns('',
             # Examples:
             url(r'^$', 'homepage.views.index', name='index'),
             url(r'^catalog/(?P<category>[male|female]+)/$',
                 'homepage.views.catalog', name='catalog'),
             url(r'^contacts/post/$', 'homepage.views.contacts_post', name='contacts-post'),
             url(r'^admin/', include(admin.site.urls)),
             url(r'', 'homepage.views.index', name='index')
             )
