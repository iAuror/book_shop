# Generated by Django 3.1.3 on 2020-12-05 08:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0009_auto_20201205_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='like',
        ),
        migrations.AddField(
            model_name='books',
            name='like',
            field=models.ManyToManyField(related_name='liked_books', to=settings.AUTH_USER_MODEL),
        ),
    ]