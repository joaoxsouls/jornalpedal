# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib.syndication.views import Feed
from django.utils.translation import ugettext as _
from django.utils.html import strip_tags

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):

    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(max_length=200, editable=False)
    order = models.IntegerField()

    def __unicode__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Post(models.Model):

    title = models.CharField(_('title'), max_length=200)
    user = models.ForeignKey(User)
    pub_date = models.DateField(_('date published'))
    category = models.ForeignKey(Category)
    content = models.TextField(_('content'))
    slug = models.SlugField(max_length=200, editable=False)
    carousel = models.BooleanField(_('carousel'))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def sinopse(self):
        content = self.content.replace('&nbsp;', ' ' * 6)
        return strip_tags(content)[0:200] + '...'


class PostFeed(Feed):

    title = _('Pedal Newspaper updates')
    link = '/'
    description = _('news articles events multimedia and editions updates of the Newspaper ')

    def items(self):
        return Post.objects.select_related('category').order_by('-pub_date')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.sinopse()

    def item_link(self, item):
        return '/' + item.category.title + '/' + item.slug


class Image(models.Model):

    image = models.ImageField(_('image'), upload_to='posts/')
    post = models.ForeignKey(Post, related_name='images')
    highlight = models.BooleanField(_('highlight'))
    carousel = models.BooleanField(_('carousel'))
    thumbnail = ImageSpecField([ResizeToFill(width=300, height=195)], image_field='image', format='JPEG', cache_to='posts/thumbs')
    mini = ImageSpecField([ResizeToFill(width=100, height=100)], image_field='image', format='JPEG', cache_to='posts/mini')
