# Generated by Django 3.0.6 on 2020-06-15 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=40),
        ),
    ]