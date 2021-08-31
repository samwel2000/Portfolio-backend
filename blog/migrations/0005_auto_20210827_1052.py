# Generated by Django 3.2.4 on 2021-08-27 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_aboutcontent_contactcontent_experiencecontent_herocontent_organization_project_skill'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Post Categories'},
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={'verbose_name_plural': 'Exp Organizations'},
        ),
        migrations.AlterField(
            model_name='organization',
            name='abbreviation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
