# Generated by Django 4.2.7 on 2023-12-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_alter_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
