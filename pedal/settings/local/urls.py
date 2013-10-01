from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from ..urls import urlpatterns

admin.autodiscover()

urlpatterns += static(settings.STATIC_URL, view='staticassets.views.serve')

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
