# Generated by Django 4.2.1 on 2023-05-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0006_remove_latestposts_category_remove_topposts_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='latestposts',
            name='excerpt',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='topposts',
            name='excerpt',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
