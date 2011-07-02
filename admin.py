from webmash.models import Page, Folder, LocalText
from django.contrib import admin

class FolderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Folder, FolderAdmin)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Page, PageAdmin)

class LocalTextAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalText, LocalTextAdmin)
