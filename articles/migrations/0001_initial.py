# Generated by Django 4.0.5 on 2024-04-23 10:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='articles/')),
                ('about', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.datetime(2024, 4, 23, 10, 28, 58, 432066, tzinfo=utc))),
                ('image', models.ImageField(upload_to='photos/articles', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('address', models.TextField(blank=True, null=True)),
                ('date_start', models.DateField(default=datetime.datetime(2024, 4, 23, 10, 28, 58, 430069, tzinfo=utc))),
                ('date_end', models.DateField(default=datetime.datetime(2024, 4, 23, 10, 28, 58, 430069, tzinfo=utc))),
                ('about', models.TextField()),
                ('image', models.ImageField(upload_to='photos/events', verbose_name='Фото')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Контактный телефон')),
                ('organization', models.CharField(blank=True, max_length=50, null=True, verbose_name='Учреждение')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('image', models.ImageField(upload_to='photos/', verbose_name='Фото')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_org', models.BooleanField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ManyToManyField(through='articles.Event_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Article_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='event',
            field=models.ManyToManyField(through='articles.Event_Article', to='articles.event'),
        ),
        migrations.AddField(
            model_name='article',
            name='user',
            field=models.ManyToManyField(through='articles.Article_User', to=settings.AUTH_USER_MODEL),
        ),
    ]
