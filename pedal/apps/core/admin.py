from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.forms import ValidationError
from django.shortcuts import render
from django.utils.translation import ugettext as _


from .models import Post, Image, Category


class ImageCustomFormset(BaseInlineFormSet):

    def clean(self):
        images = [image_form for image_form in self.forms
                  if hasattr(image_form, 'cleaned_data')
                  and 'highlight' in image_form.cleaned_data
                  and image_form.cleaned_data['highlight']]
        if len(images) != 1:
            raise ValidationError(_('Post must have one image highlight'))
        super(ImageCustomFormset, self).clean()


class ImageInline(admin.StackedInline):

    model = Image
    extra = 1
    formset = ImageCustomFormset


class PostAdmin(admin.ModelAdmin):

    list_display = ['title', 'pub_date', 'category', 'user', 'carousel']
    inlines = [ImageInline]
    list_editable = ['carousel']
    list_filter = ['category', 'user', 'carousel']
    date_hierarchy = 'pub_date'
    search_fields = ['category__title', 'user__username', 'user__first_name', 'user__last_name', 'title', ]
    ordering = ['-pub_date']

    class Media:
        js = ("ckeditor/ckeditor.js", "ckeditor/config.js")

    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        return patterns('', url(r'^(?P<post_id>\d+)/get_pics/$', self.admin_site.admin_view(self.get_post_pics)),) + urls

    def get_post_pics(self, request, post_id):
        query = Post.objects.get(id=post_id).images.all()
        images = [(str(image.image.url), image.id, image.image.width) for image in query]
        minis = [(str(image.mini.url), image.id) for image in query]
        return render(request, 'admin/get_post_pics.html', {'images': images, 'minis': minis})

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
