# Generated by Django 3.2.6 on 2021-08-25 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_remove_sectionmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionmodel',
            name='bio_description',
            field=models.TextField(default='hello', null=True),
        ),
    ]
