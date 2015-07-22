# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0002_auto_20150718_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'stories'},
        ),
        migrations.AddField(
            model_name='story',
            name='voters',
            field=models.ManyToManyField(related_name='liked_stories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='moderator',
            field=models.ForeignKey(related_name='moderated_stories', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='story',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
