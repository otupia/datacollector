# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 09:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('height', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
                ('url', models.CharField(max_length=300)),
                ('filepath', models.CharField(max_length=300)),
                ('status', models.CharField(choices=[('00', '默认值'), ('01', '数据已录入,未下载'), ('100', '数据可用'), ('999', '数据删除')], default='00', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('00', '默认值'), ('01', '数据已录入,未下载'), ('02', '详情未下载'), ('03', '未建立关联'), ('100', '数据可用'), ('999', '数据删除')], default='00', max_length=200)),
                ('related_tags', models.ManyToManyField(related_name='_tag_related_tags_+', to='keyword_img.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='TagImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyword_img.KeywordImg')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keyword_img.Tag')),
            ],
        ),
    ]
