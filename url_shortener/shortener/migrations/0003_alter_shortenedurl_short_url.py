# Generated by Django 5.1.4 on 2025-01-11 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_remove_shortenedurl_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_url',
            field=models.CharField(max_length=6, null=True, unique=True),
        ),
    ]
