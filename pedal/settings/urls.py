from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.generic import RedirectView

admin.autodiscover()


class TextPlainView(TemplateView):

    def render_to_response(self, context, **kwargs):
        return super(TextPlainView, self).render_to_response(context, content_type='text/plain', **kwargs)

urlpatterns = patterns('',
    url(r'^admin/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('pedal.apps.editions.urls', 'editions')),
    url(r'^robots\.txt$', TextPlainView.as_view(template_name='robots.txt')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/pedal/img/favicon.ico')),
    url(r'^', include('pedal.apps.core.urls', 'core'))
)
