# Generated by Django 5.1.4 on 2025-01-11 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0006_remove_analytics_ip_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='analytics',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
