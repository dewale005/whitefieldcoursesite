# Generated by Django 3.2.6 on 2021-08-25 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_coursesmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesmodel',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
