# Generated by Django 5.0.2 on 2024-02-14 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_options_room_paricipants'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='paricipants',
            new_name='participants',
        ),
    ]
