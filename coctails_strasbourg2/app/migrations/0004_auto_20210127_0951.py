# Generated by Django 3.1.5 on 2021-01-27 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_cocktailingredientunit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cocktailingredientunit",
            name="unit",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.unit",
            ),
        ),
    ]
