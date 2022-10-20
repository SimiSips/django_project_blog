from django.utils import timezone
from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=240, unique=True)
    url = models.CharField(max_length=240)
    image_url = models.CharField(max_length=240)
    img = models.FileField(upload_to='books/', default='BOOK IMAGE')

class Post(models.Model):
    STATUS_CHOICES =(
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=240, unique=True)
    body = models.CharField(max_length=240)
    img = models.FileField(upload_to='posts/', default='POST IMAGE')
    slug = models.SlugField(max_length=240, unique_for_date="publish")
    publish = models.DateField(default=timezone.now)
    author = models.CharField(max_length=240)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')


    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

class Farm(models.Model):
    holding_id = models.IntegerField(unique=True)
    zone = models.CharField(max_length=3)
    brand = models.CharField(max_length=240)
    dob = models.DateField()
    species = models.CharField(max_length=240)
    breed = models.CharField(max_length=240)
    sex = models.CharField(max_length=240)
    age = models.IntegerField()
    colour = models.CharField(max_length=240)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField()

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'comment by {self.name} on {self.post}'
    