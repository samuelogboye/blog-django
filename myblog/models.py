from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# from django.utils.text import slugify



class Profile(models.Model):
     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
     bio = models.TextField()

     def __str__(self):
          return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
           return self.name

    def get_absolute_url(self):
            return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=200)
    header_image = models.FileField(null=True, blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    # body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200, default='uncategorized')
    likes = models.ManyToManyField(User, related_name='blog_posts')
    comment = models.TextField()

    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=(str(self.id),))
        # return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)