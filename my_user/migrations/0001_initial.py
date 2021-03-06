# Generated by Django 3.1.5 on 2021-04-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userregisterform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.EmailField(max_length=254, verbose_name='email address')),
                ('email2', models.EmailField(max_length=254, verbose_name='email address')),
                ('place_of_residence', models.CharField(max_length=20, verbose_name='place of living')),
                ('current_living_place', models.CharField(max_length=20, verbose_name='where you are living now')),
            ],
        ),
    ]
