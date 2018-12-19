# Generated by Django 2.1 on 2018-08-30 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('title', models.CharField(max_length=200)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.FileField(upload_to='')),
                ('details', models.TextField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=200)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('image', models.FileField(upload_to='')),
                ('venue', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category')),
                ('events_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.author')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.category'),
        ),
    ]
