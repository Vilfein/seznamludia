# Generated by Django 4.2.2 on 2023-06-27 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clovek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=20)),
                ('prijmeni', models.CharField(max_length=20)),
                ('vek', models.IntegerField()),
            ],
        ),
    ]
