# Generated by Django 4.2.7 on 2023-11-28 18:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=ckeditor.fields.RichTextField(),
        ),
    ]