# Generated by Django 5.2.3 on 2025-06-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_delivary_cost_config_delivery_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='about_page',
            field=models.TextField(blank=True, null=True),
        ),
    ]
