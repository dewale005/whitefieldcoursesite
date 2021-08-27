# Generated by Django 3.2.6 on 2021-08-24 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210824_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('tutor', 'Tutor'), ('admin', 'Admin')], default='student', max_length=255),
        ),
    ]
