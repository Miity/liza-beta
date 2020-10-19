from django.db import models

# Create your models here.

class Menu(models.Model):
    status = models.BooleanField("Опубликовать?", default=True)
    title = models.CharField("Название", max_length=200)
    url = models.CharField("Сылка", max_length=200)