# Generated by Django 3.2.4 on 2021-10-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20211002_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='share_count',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
