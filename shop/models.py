from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Bikes(models.Model):
    name = models.CharField(max_length=35, default="Shimano")
    size = models.CharField(max_length=2, default=26)
    color = models.CharField(max_length=10, default="Blu")
    description = models.TextField(default="bicklete")
    full_description = RichTextField(blank=True, null=True)
    price = models.CharField(max_length=5, default=0)
    image = models.ImageField(default="defalut.png")
    age_category = models.CharField(default=16, max_length=15)
    bike_categories = models.CharField(default="BMX", max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Bikes'


class Images(models.Model):
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Images'
