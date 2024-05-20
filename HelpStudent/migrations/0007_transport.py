# Generated by Django 5.0.2 on 2024-05-10 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HelpStudent', '0006_logement_prix'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=100)),
                ('departure_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('vehicle', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
