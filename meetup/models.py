import datetime

from django.db import models


# Create your models here.
class Files(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.datetime.now())
    file = models.FileField(upload_to="files",)

    def __str__(self):
        return f'{self.name} - {self.slug} -{self.description}'


class ResultML(models.Model):
    ip_src = models.CharField(max_length=200)
    port_src = models.CharField(max_length=200)
    ip_des = models.CharField(max_length=200)
    port_des = models.CharField(max_length=200)
    classification = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.ip_src} - {self.port_src} - {self.ip_des} - {self.port_des} - {self.classification}'
