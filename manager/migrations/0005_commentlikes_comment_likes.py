# Generated by Django 3.1.3 on 2020-12-15 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_books_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentlikes',
            name='comment_likes',
            field=models.IntegerField(default=0),
        ),
    ]
