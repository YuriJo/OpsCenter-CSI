# Generated by Django 4.2.7 on 2023-12-07 07:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("DjOpsCenter", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Client",
            new_name="Clients",
        ),
        migrations.RenameModel(
            old_name="Command",
            new_name="Commands",
        ),
    ]
