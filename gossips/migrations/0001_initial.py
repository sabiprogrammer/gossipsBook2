# Generated by Django 3.1.4 on 2020-12-31 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gossips.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55, unique=True)),
                ('description', models.TextField(blank=True, help_text='You can optionally provide a description for this tag', max_length=300, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='GossipsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='What is the title of your gossip?', max_length=75, unique=True, verbose_name='Title')),
                ('content', models.TextField(max_length=3000)),
                ('slug', models.SlugField(unique=True)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('image', models.ImageField(blank=True, help_text='Add image (optional)', null=True, upload_to=gossips.models.upload_location)),
                ('shares', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gossip_author', to=settings.AUTH_USER_MODEL)),
                ('false', models.ManyToManyField(blank=True, related_name='false', to=settings.AUTH_USER_MODEL)),
                ('q_tags', models.ManyToManyField(blank=True, to='gossips.Tags')),
                ('true', models.ManyToManyField(blank=True, related_name='true', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Gossips',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('date_published', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('gossip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gossips.gossipsmodel')),
            ],
            options={
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
