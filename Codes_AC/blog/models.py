from django.db import models


class Post(models.Model):
    sno = models.AutoField(primary_key = True)
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"Blog of {self.author}"
    