from webmash.models import *
from django.contrib import admin

class FolderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('related_items',)
admin.site.register(Folder, FolderAdmin)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ('related_items',)
admin.site.register(Page, PageAdmin)

class LocalHTMLAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalHTML, LocalHTMLAdmin)

class LocalImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalImage, LocalImageAdmin)

class LocalTextAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalText, LocalTextAdmin)
