# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InterrogationRoomTable',
            fields=[
                ('room_id', models.AutoField(primary_key=True, serialize=False, verbose_name='审讯室id')),
                ('connection_number', models.IntegerField()),
                ('url_type', models.IntegerField()),
                ('original_url', models.URLField()),
                ('smart_url', models.URLField()),
                ('creat_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('interrogate_status', models.BooleanField(default=False, verbose_name='状态')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户id')),
                ('user_name', models.CharField(max_length=32, unique=True, verbose_name='用户名称')),
                ('user_pwd', models.CharField(max_length=32, verbose_name='用户密码')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('login_time', models.DateTimeField(blank=True, null=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('permission', models.IntegerField(blank=True, default=0)),
                ('login_state', models.IntegerField(blank=True, default=0)),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
            ],
        ),
        migrations.AddField(
            model_name='interrogationroomtable',
            name='add_person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.User'),
        ),
    ]
