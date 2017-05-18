from django.contrib import admin
from homepage.models import *
# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'category', 'sorting']
    fields = ('title', 'img', 'image_tag', 'category', 'sorting')
    readonly_fields = ('image_tag',)


class ShoesTypeAdmin(admin.ModelAdmin):
    pass


class ContactsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catalog, CatalogAdmin)
admin.site.register(ShoesType, ShoesTypeAdmin)
admin.site.register(Contacts, ContactsAdmin)
