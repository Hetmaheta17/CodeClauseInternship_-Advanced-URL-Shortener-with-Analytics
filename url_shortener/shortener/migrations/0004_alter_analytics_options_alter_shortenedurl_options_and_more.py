# Generated by Django 5.1.4 on 2025-01-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_shortenedurl_short_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analytics',
            options={'verbose_name': 'Analytics Record', 'verbose_name_plural': 'Analytics Records'},
        ),
        migrations.AlterModelOptions(
            name='shortenedurl',
            options={'verbose_name': 'Shortened URL', 'verbose_name_plural': 'Shortened URLs'},
        ),
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_url',
            field=models.CharField(db_index=True, max_length=6, null=True, unique=True),
        ),
    ]
