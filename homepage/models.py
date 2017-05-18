from django.db import models
import uuid
import os
import time
# Create your models here.


def get_file_path_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s/%s.%s" % (time.strftime("%Y/%m/%d"), uuid.uuid4(), ext)
    return os.path.join('img/', filename)


class ShoesType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Catalog(models.Model):
    title = models.CharField(max_length=255)
    # desc = models.TextField()
    img = models.ImageField(upload_to=get_file_path_img, default='',
                            blank=True, null=True, max_length=255)
    category = models.ForeignKey('ShoesType', blank=True, null=True)
    sorting = models.IntegerField(default=0)

    def image_tag(self):
        try:
            return u'<img src="%s" style="height:70px"/>' % self.img.url
        except ValueError:
            return u'<img src="http://lorax-d.com.ua/bitrix/templates/main/img/noimg.jpg" style="height:70px"/>'
    image_tag.allow_tags = True

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    massage = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
