from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    location =models.CharField(max_length=100)
    created_on =models.DateTimeField(auto_now_add=True)
    image = models.FileField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse("index")

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=50)
    created_on =models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        unique=True,
        editable=False,
        max_length=100
    )

    def get_absolute_url(self):
        return reverse("languages")

    def save(self,*args,**kwargs):
        value = self.name
        self.slug = slugify(value,allow_unicode=True)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    age =models.IntegerField()
    company =models.ForeignKey(Company,on_delete=models.CASCADE)
    language =models.ManyToManyField(Language,related_name="language")
    created_on =models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        unique=True,
        max_length=50,
        editable=False
        )

    def get_absolute_url(self):
        return reverse("index")

    def save(self,*args,**kwargs):
        value = self.name
        self.slug = slugify(value,allow_unicode=True)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name                    

