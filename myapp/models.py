from django.db import models
from django.db.models import Q


# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FullWidth(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    url = models.URLField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name

class SidebarLeft(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    url = models.URLField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name

class SidebarRight(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    url = models.URLField(max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.name

class Uchlik(models.Model):
    name_uz = models.CharField(max_length=100, blank=True)
    #name = models.CharField(max_length=100)
    name_ru = models.CharField(max_length=100,blank=True)
    name_en = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='myapp/images/')
    description_uz = models.CharField(max_length=100,blank=True)
    #description = models.CharField(max_length=100)
    description_ru = models.CharField(max_length=100,blank=True)
    description_en = models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.name_uz

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "cities"

    def __str__(self):
        return self.name