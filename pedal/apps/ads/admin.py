from django.contrib import admin

from .models import Ad


class AdAdmin(admin.ModelAdmin):

    list_display = ['name', 'image', 'url', 'highlight']
    list_editable = ['highlight']

    def save_model(self, request, obj, form, change):
        if obj.highlight:
            highlighted_ads = Ad.objects.filter(highlight=True).exclude(id=obj.id)
            for ad in highlighted_ads:
                ad.highlight = False
                ad.save()
        obj.save()

admin.site.register(Ad, AdAdmin)
