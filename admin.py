from webmash.models import *
from django.contrib import admin

class FolderAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Folder, FolderAdmin)

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Page, PageAdmin)

class LocalImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalImage, LocalImageAdmin)

class LocalTextAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(LocalText, LocalTextAdmin)
