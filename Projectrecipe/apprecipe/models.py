from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe-detail', args=(str(self.id)))


class Post(models.Model):
    recipe_tittle = models.CharField(max_length=50, unique=True, verbose_name="Название")
    recipe = RichTextField(blank=True, null=True, config_name='default', verbose_name="Рецепт")
    #recipe = models.TextField(verbose_name="Рецепт")
    #author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    recipe_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50, verbose_name="Категория")
    image = models.ImageField(null=True, blank=True, upload_to="images/", default='default.jpg')

    def save(self, *args, **kwargs):
        self.recipe_tittle = self.recipe_tittle.lower()
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.recipe_tittle

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
       # return reverse('recipe-detail', args=(str(self.pk)))
        return reverse('home')
