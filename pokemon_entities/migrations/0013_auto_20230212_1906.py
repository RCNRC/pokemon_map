# Generated by Django 2.2.24 on 2023-02-12 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_pokemon_next_evolution'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='next_evolution',
            new_name='previous_evolution',
        ),
    ]
