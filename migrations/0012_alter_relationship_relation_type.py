# Generated by Django 3.2.23 on 2024-01-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_schema_plugin', '0011_alter_relationship_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='relation_type',
            field=models.CharField(default='Type', max_length=255),
        ),
    ]