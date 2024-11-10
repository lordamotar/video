from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)  # Ссылка на проект (опционально)
    video_url = models.URLField(blank=True, null=True)  # Ссылка на видео (например, YouTube)
    images = models.ImageField(upload_to='portfolio/', blank=True, null=True)  # Основное изображение
    date_completed = models.DateField()
    categories = models.ManyToManyField(Category, related_name='projects')

    def __str__(self):
        return self.title
