# Generated by Django 3.1.3 on 2020-12-22 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0008_remove_comment_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TMPBooks',
            fields=[
                ('title', models.CharField(max_length=100, verbose_name='Оглавление')),
                ('text', models.TextField(verbose_name='Текст книги')),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, verbose_name='Рейтинг')),
                ('count_rate_users', models.PositiveIntegerField(default=0)),
                ('rate_all_stars', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('author', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.genre', verbose_name='Жанр')),
                ('ratting', models.ManyToManyField(related_name='tmp_book_rating', through='manager.BookRating', to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.pub_office')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.AddField(
            model_name='bookrating',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to='manager.tmpbooks'),
        ),
        migrations.AddField(
            model_name='comment',
            name='tmp_book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='manager.tmpbooks'),
        ),
    ]