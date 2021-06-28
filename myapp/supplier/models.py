from django.db import models
import random
import os
from io import BytesIO
from django.core.files import File
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from datetime import datetime  


# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)

    return name, ext


def upload_image_path_supplier(instance, filename):
    new_filename = random.randint(1, 23243423)
    name, ext = get_filename_ext(filename)
    final_filename ='{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)

    #return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

    return "supplier/{final_filename}".format(final_filename=final_filename)


class Supplier(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_image_path_supplier, null=True, blank=True)
    thumbnail = models.ImageField(upload_to=upload_image_path_supplier, null=True, blank=True)
    ordering = models.IntegerField(default=1)
    available = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(default=datetime.now())
    updated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_slural = 'Supplier'

    class Meta:
        ordering = ('name',)

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

    def save(self, *args, **kwargs):
        self.thumbnail = self.make_thumbnail(self.image)

        super().save(*args, **kwargs)

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail