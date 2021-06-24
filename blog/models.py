from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=256)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    c_author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=256)
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.post.pk})
