# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 16:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(b'code works', b'code works'), (b'code compiles', b'code compiles'), (b'code fail', b'code fail')], max_length=100, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441')),
                ('content', models.TextField(verbose_name='\u041a\u043e\u0434 \u0440\u0435\u0448\u0435\u043d\u0438\u044f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u041e\u043f\u0443\u0431\u043b\u0438\u043a\u043e\u0432\u0430\u043d\u043e')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to=settings.AUTH_USER_MODEL, verbose_name='\u0410\u0432\u0442\u043e\u0440')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': '\u0420\u0435\u0448\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0420\u0435\u0448\u0435\u043d\u0438\u044f',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', models.CharField(max_length=255, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('input_example', models.CharField(max_length=100, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0440 \u0432\u0432\u043e\u0434\u0430')),
                ('output_example', models.CharField(max_length=100, verbose_name='\u041f\u0440\u0438\u043c\u0435\u0440 \u0432\u044b\u0432\u043e\u0434\u0430')),
            ],
            options={
                'verbose_name': '\u0417\u0430\u0434\u0430\u0447\u0430',
                'verbose_name_plural': '\u0417\u0430\u0434\u0430\u0447\u0438',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_input', models.CharField(max_length=100, verbose_name='\u0412\u0445\u043e\u0434\u044f\u0449\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u0435')),
                ('expected_output', models.CharField(max_length=100, verbose_name='\u041e\u0436\u0438\u0434\u0430\u0435\u043c\u044b\u0439 \u0432\u044b\u0432\u043e\u0434')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='tasks.Task', verbose_name='\u0417\u0430\u0434\u0430\u0447\u0430')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0441\u0442',
                'verbose_name_plural': '\u0422\u0435\u0441\u0442\u044b',
            },
        ),
        migrations.AddField(
            model_name='solution',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='tasks.Task', verbose_name='\u0417\u0430\u0434\u0430\u0447\u0430'),
        ),
    ]
