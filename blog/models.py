from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from markdownx.models import MarkdownxField

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    featured_image = models.ImageField(upload_to='blog/', blank=True)
    is_published = models.BooleanField(default=True)
    content = MarkdownxField() 
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']