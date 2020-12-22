# Generated by Django 3.1.4 on 2020-12-22 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheaters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheatersmodel',
            name='title',
            field=models.CharField(help_text='What is the title of your cheater story?', max_length=255, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
