from webmash.models import Page, Folder, LocalText
from django.contrib import admin

admin.site.register(Folder)
admin.site.register(Page)

class LocalTextAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalText, LocalTextAdmin)
