from django.db import models

class Pricing(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='pricing_images/', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Index(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='index_images/', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главные страницы"
