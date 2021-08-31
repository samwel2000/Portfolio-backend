# Generated by Django 3.2.4 on 2021-08-27 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210614_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section1', models.TextField()),
                ('section2', models.TextField()),
                ('section3', models.TextField()),
                ('photo', models.ImageField(upload_to='about')),
            ],
            options={
                'verbose_name_plural': 'About Content',
            },
        ),
        migrations.CreateModel(
            name='ContactContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Content',
            },
        ),
        migrations.CreateModel(
            name='HeroContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio_header', models.CharField(max_length=1000)),
                ('bio_content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Hero Content',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=1000)),
                ('abbreviation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='project')),
                ('project_setting', models.CharField(default='featured project', max_length=300)),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('project_stack', models.TextField(help_text='Enter stack separated by a cooma')),
                ('project_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('github_link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=1000)),
                ('skill_liist', models.TextField(help_text='Enter skills separated by a comma')),
            ],
        ),
        migrations.CreateModel(
            name='ExperienceContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=1000)),
                ('dates', models.CharField(max_length=100)),
                ('duties', models.TextField(help_text='Enter duties separated by a cooma')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.organization')),
            ],
            options={
                'verbose_name_plural': 'Experience Content',
            },
        ),
    ]
