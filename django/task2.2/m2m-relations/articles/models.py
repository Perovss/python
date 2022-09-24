from django.db import models

class Article(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

class Tags(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=256, verbose_name='Название Раздел')


    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.title
