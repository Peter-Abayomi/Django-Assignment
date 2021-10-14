from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=50)
    display_content = models.CharField(max_length=200)
    content = models.TextField()
    another_content = models.TextField()
    another_image = models.ImageField(upload_to='images')
    category = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images')
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class FrontImage(models.Model):
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image
