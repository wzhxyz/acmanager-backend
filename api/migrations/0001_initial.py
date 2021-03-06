# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-03-13 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields.related


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tongji',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oj_name', models.CharField(max_length=15)),
                ('problem_id', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('realName', models.CharField(max_length=20, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('vjname', models.CharField(max_length=20, null=True)),
                ('uvaId', models.CharField(max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.fields.related.ForeignKey, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tongji',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tongji', to='api.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='tongji',
            unique_together=set([('user', 'oj_name', 'problem_id')]),
        ),
    ]
