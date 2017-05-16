from django.contrib import admin
from homepage.models import *
# Register your models here.


class CatalogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Catalog, CatalogAdmin)
