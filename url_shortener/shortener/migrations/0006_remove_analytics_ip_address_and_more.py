# Generated by Django 5.1.4 on 2025-01-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_alter_analytics_options_alter_shortenedurl_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analytics',
            name='ip_address',
        ),
        migrations.AlterField(
            model_name='analytics',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
