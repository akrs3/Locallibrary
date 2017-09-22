# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter a the book's natutal language (e.g English, Portugese, French)", max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back']},
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
