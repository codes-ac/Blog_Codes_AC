# Generated by Django 3.0.6 on 2020-06-15 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=40),
        ),
    ]
