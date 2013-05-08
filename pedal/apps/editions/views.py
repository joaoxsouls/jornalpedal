from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from ..core.views import SideBarContentMixin, PaginatorMixin
from ..editions.models import Edition


class EditionListingView(SideBarContentMixin, PaginatorMixin, ListView):

    context_object_name = 'editionlist'
    queryset = Edition.objects.all().order_by('-number')
    paginate_by = 6
    template_name = 'core/edition_listing.html'


class ReaderView(TemplateView):

    template_name = 'core/reader.html'

    def get_context_data(self, **kwargs):
        ctx = super(ReaderView, self).get_context_data(**kwargs)
        number = self.kwargs.get('number', 1)
        ctx['edition'] = get_object_or_404(Edition, number=number)
        ctx['selected'] = 'editions'
        return ctx
