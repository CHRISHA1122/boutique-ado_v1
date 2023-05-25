# Generated by Django 4.2.1 on 2023-05-25 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="product",
            name="has_sizes",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
