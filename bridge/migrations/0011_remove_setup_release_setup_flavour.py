# Generated by Django 4.2.9 on 2024-01-22 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bridge", "0010_rename_flavous_definition_flavours"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="setup",
            name="release",
        ),
        migrations.AddField(
            model_name="setup",
            name="flavour",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="setups",
                to="bridge.flavour",
            ),
            preserve_default=False,
        ),
    ]
