from django.contrib import admin
from .models import Supplier
# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'available',  'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    readonly_fields = ('thumbnail','created_at','updated_at', )


admin.site.register(Supplier,SupplierAdmin)