from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=20, default=0)
    desc = models.CharField(max_length=2000)
    datestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"Message from {self.name}"
