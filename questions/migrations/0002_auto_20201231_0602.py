# Generated by Django 3.1.4 on 2020-12-31 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsmodel',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
