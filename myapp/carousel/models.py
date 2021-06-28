from django.db import models
from products.models import Category
import random
import os
from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
from django.contrib.auth.models import User

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)

    return name, ext


def upload_image_path_carousel(instance, filename):
    new_filename = random.randint(1, 23243423)
    name, ext = get_filename_ext(filename)
    final_filename ='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)

    #return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

    return "carousel/{final_filename}".format(final_filename=final_filename)
    # end create path and images

# Create your models here.

class Parent(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
   
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


class Carousel(models.Model):
    parent = models.ForeignKey(Parent, related_name='carousel', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    link = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path_carousel, null=True, blank=True)
    available = models.BooleanField(default=False)
   
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)