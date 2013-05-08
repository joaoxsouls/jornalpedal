from django.contrib import admin

from .models import Edition


class EditionAdmin(admin.ModelAdmin):

    list_display = ['number', 'month', 'highlight']
    list_editable = ['highlight']
    search_fields = ['number', 'month']

    def save_model(self, request, obj, form, change):
        if obj.highlight:
            highlighted_editions = Edition.objects.filter(highlight=True).exclude(id=obj.id)
            for edition in highlighted_editions:
                edition.highlight = False
                edition.save()
        obj.save()

admin.site.register(Edition, EditionAdmin)
