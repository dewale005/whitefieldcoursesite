# Generated by Django 3.2.6 on 2021-08-25 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20210825_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesmodel',
            name='lectures',
            field=models.ManyToManyField(to='course.SectionModel'),
        ),
        migrations.AddField(
            model_name='sectionmodel',
            name='lessons',
            field=models.ManyToManyField(to='course.LessonModel'),
        ),
        migrations.AddField(
            model_name='sectionmodel',
            name='description',
            field=models.TextField(null=True),
        ),
    ]