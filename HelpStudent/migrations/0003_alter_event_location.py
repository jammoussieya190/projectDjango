# Generated by Django 5.0.2 on 2024-04-30 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpStudent', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]