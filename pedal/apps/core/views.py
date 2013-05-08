# coding: utf-8
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from .models import Post, Image
from ..editions.models import Edition
from ..ads.models import Ad


class SideBarContentMixin(object):

    def get_context_data(self, **kwargs):
        ctx = super(SideBarContentMixin, self).get_context_data(**kwargs)
        ctx['aid'] = Ad.objects.filter(highlight=True)[0]
        ctx['edition'] = Edition.objects.filter(highlight=True)[0]
        return ctx


class PaginatorMixin(object):

    def paginate_queryset(self, queryset, page_size):
        paginator = self.get_paginator(queryset, page_size, allow_empty_first_page=self.get_allow_empty())
        page_number = self.request.GET.get('p', 1)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        return (paginator, page, page.object_list, page.has_other_pages())


class HomeView(SideBarContentMixin, TemplateView):

    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['carousel'] = Post.objects.filter(carousel=True, images__carousel=True).order_by('-pub_date').prefetch_related('images').select_related('category')
        for post in ctx['carousel']:
            post.carousel_image = post.images.all()[0].image.url

        ctx['postlist'] = Post.objects.filter(images__highlight=True).order_by('-pub_date').prefetch_related('images').select_related('category', 'user')[:6]
        for post in ctx['postlist']:
            post.thumbnail_image = post.images.all()[0].thumbnail.url
            return ctx


class PostDetailView(SideBarContentMixin, DetailView):

    context_object_name = 'post'

    def get_object(self, queryset=None):
        category = self.kwargs.get('category')
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(Post.objects.select_related('category', 'user'), category__slug=category, slug=slug)
        obj.header_image = Image.objects.filter(post=obj, highlight=True)[0].image.url
        return obj


class PostListView(SideBarContentMixin, PaginatorMixin, ListView):

    context_object_name = 'postlist'
    template_name = 'core/post_listing_category.html'
    paginate_by = 6
    allow_empty = False

    def get_queryset(self):
        category = self.kwargs['category']
        queryset = Post.objects.filter(category__slug=category).order_by('-pub_date').prefetch_related('images').select_related('category')
        for post in queryset:
            post.thumbnail_image = post.images.all()[0].thumbnail.url
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(PostListView, self).get_context_data(**kwargs)
        ctx['category'] = self.kwargs.get('category')
        return ctx


class PostSearchView(SideBarContentMixin, PaginatorMixin, ListView):

    context_object_name = 'postlist'
    template_name = 'core/post_listing_search.html'
    paginate_by = 6

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        search_terms = "|".join(q.split())
        ts_vector = '''to_tsvector('portuguese', (COALESCE("core_post"."title",'') || '' || COALESCE("core_post"."content", '')))'''
        ts_query = u"to_tsquery('portuguese', '{0}')".format(search_terms)
        #ts_rank = u"ts_rank_cd({0}, {1})".format(ts_vector, ts_query)
        queryset = Post.objects.extra(
            select={'rank': u'ts_rank_cd({0}, {1})'.format(ts_vector, ts_query)},
            where=[u'{0} @@ {1}'.format(ts_vector, ts_query)],
            order_by=['-rank']
        ).prefetch_related('images').select_related('category')
        for post in queryset:
            post.thumbnail_image = post.images.all()[0].thumbnail.url
        return queryset

    def get_context_data(self, **kwargs):
        ctx = super(PostSearchView, self).get_context_data(**kwargs)
        ctx['query'] = self.request.GET.get('q', '')
        return ctx


class AboutPage(SideBarContentMixin, TemplateView):

    template_name = 'core/about_page.html'

    def get_context_data(self, **kwargs):
        ctx = super(AboutPage, self).get_context_data(**kwargs)
        ctx['post'] = Post.objects.get(category__title='pedal')
        return ctx
