from django.db import models
import uuid
import os
import time
# Create your models here.


def get_file_path_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s/%s.%s" % (time.strftime("%Y/%m/%d"), uuid.uuid4(), ext)
    return os.path.join('img/', filename)


class Catalog(models.Model):
    title = models.CharField(max_length=255)
    # desc = models.TextField()
    img = models.ImageField(upload_to=get_file_path_img, default='')
    # category = models.ManyToManyField('Category')

    # def image_tag(self):
    #     return u'<img src="%s" height="100"/>' % self.img.url
    # image_tag.allow_tags = True

    class Meta:
        ordering = ["-id"]
