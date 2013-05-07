from django.conf.urls import patterns
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from ..urls import urlpatterns

admin.autodiscover()

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
