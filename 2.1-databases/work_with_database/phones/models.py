from django.db import models
from django.utils.text import slugify

class Phone(models.Model):
    id = models.AutoField(primary_key=True)  # Основной ключ модели
    name = models.CharField(max_length=255)  # Название телефона
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    image = models.URLField()  # Ссылка на изображение
    release_date = models.DateField()  # Дата выпуска
    lte_exists = models.BooleanField()  # Наличие LTE
    slug = models.SlugField(max_length=255, unique=True, blank=True)  # Slug для URL

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Генерация slug из названия
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
