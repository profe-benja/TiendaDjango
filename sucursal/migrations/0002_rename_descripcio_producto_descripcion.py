# Generated by Django 4.2.1 on 2023-05-31 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sucursal", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="producto", old_name="descripcio", new_name="descripcion",
        ),
    ]