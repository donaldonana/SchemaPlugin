# Generated by Django 3.2.23 on 2024-01-25 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd_schema_plugin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='property',
            field=models.TextField(default='{}'),
        ),
        migrations.AlterField(
            model_name='node',
            name='labels',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='node',
            name='name',
            field=models.CharField(default='Name', max_length=255),
        ),
        migrations.AlterField(
            model_name='node',
            name='type',
            field=models.CharField(default='Type', max_length=255),
        ),
    ]