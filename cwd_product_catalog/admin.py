from django.contrib import admin
from django.conf import settings as django_settings
from cms.admin.placeholderadmin import PlaceholderAdmin
from product_catalog.models import CWDProduct, Category

class CWDProductAdmin(PlaceholderAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ('name',)
    list_filter = ('category', )

class CategoryAdmin(PlaceholderAdmin):
    prepopulated_fields = {"slug": ("name",)}
    pass


admin.site.register(CWDProduct, CWDProductAdmin)
admin.site.register(Category, CategoryAdmin)
