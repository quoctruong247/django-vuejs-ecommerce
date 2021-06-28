from django.contrib import admin
from .models import Carousel, Parent
# Register your models here.

class CarouselAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'available', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    

admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Parent)