# Generated by Django 3.1.3 on 2022-03-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_question_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='questions',
            field=models.ManyToManyField(to='onlinecourse.Question'),
        ),
    ]
