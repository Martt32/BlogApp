from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    title = models.CharField(max_length=1000, null=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    content = models.TextField(max_length=5000000, null=True)
    date = models.CharField(null=True, max_length=255)
    photo = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 

    def __str__(self):
        return self.title