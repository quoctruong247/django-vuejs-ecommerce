from django.contrib import admin
from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'available', 'feature', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    change_form_template = 'admin/category/edit.html'
    change_list_template = 'admin/category/list.html'
    search_fields = ['name']
    readonly_fields = ('thumbnail',)
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'price','priceRange', 'image', 'available', 'feature', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    readonly_fields = ('thumbnail','created_at','updated_at', 'last_visit','num_visits',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'image', 'thumbnail', ]
    readonly_fields = ('thumbnail', )


admin.site.site_header = "TSDI - Admin Tutorial Dashboard"
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductReview)