# Generated by Django 3.2.6 on 2021-08-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_coursesmodel_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesmodel',
            name='description',
            field=models.TextField(null=True),
        ),
    ]