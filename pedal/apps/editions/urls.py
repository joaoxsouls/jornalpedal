from django.conf.urls import patterns, url


from . import views

urlpatterns = patterns('',
    url(r'^edicoes/$', views.EditionListingView.as_view(), name='edition_listing'),
    url(r'^leitor/$', views.ReaderView.as_view(), name='reader'),
    url(r'^leitor/edicao/(?P<number>\d+)$', views.ReaderView.as_view(), name='reader_edition'),
)
