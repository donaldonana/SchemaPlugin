# Generated by Django 3.2.23 on 2024-01-25 23:08

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_schema_plugin', '0004_alter_node_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='labels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=list, size=None),
        ),
    ]
