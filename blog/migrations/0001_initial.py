# Generated by Django 3.2.4 on 2021-06-14 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=250, unique_for_date='created')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='published', max_length=100)),
                ('category', models.ManyToManyField(to='blog.Category')),
            ],
            options={
                'verbose_name_plural': 'Posts',
                'ordering': ('-created',),
            },
        ),
    ]