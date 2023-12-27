from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default='default.jpg')
    title = models.CharField(max_length=300)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    #tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_date']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
    
    
    def __str__(self) -> str:
        return self.title
    