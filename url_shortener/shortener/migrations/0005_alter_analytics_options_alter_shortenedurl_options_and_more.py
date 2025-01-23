# Generated by Django 5.1.4 on 2025-01-11 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0004_alter_analytics_options_alter_shortenedurl_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analytics',
            options={},
        ),
        migrations.AlterModelOptions(
            name='shortenedurl',
            options={},
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_url',
            field=models.CharField(max_length=6, null=True, unique=True),
        ),
    ]
