from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.views.generic import RedirectView

from . import views
from .models import PostFeed

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='temp.html')),
    url(r'^feed/$', PostFeed(), name='feed'),
    url(r'^testintestin/$', views.HomeView.as_view(), name='home'),
    url(r'^pesquisa/$', views.PostSearchView.as_view(), name='search'),
    url(r'^pedal/$', views.AboutPage.as_view(), name='about'),
    url(r'^loja/$', RedirectView.as_view(url='http://www.jornalpedal.bigcartel.com/'), name='shop'),
    url(r'^(?P<category>[a-z]+)/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^(?P<category>[-\w]+)/$', views.PostListView.as_view(), name='post_listing'),
)
