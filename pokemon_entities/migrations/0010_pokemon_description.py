# Generated by Django 2.2.24 on 2023-02-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20230212_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
