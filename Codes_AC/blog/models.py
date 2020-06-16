from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")
    content = models.TextField()
    pub_date = models.DateTimeField()
    slug = models.CharField(max_length=140)

    def __str__(self):
        return f"Blog of {self.author}"


class BlogComment(models.Model):
    sno = models.AutoField(primary_key = True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    