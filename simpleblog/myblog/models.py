from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
           return self.name

    def get_absolute_url(self):
            # return reverse('article-detail', args=(str(self.id),))
            return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, default='uncategorized')

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id),))
        # return reverse('home')
