# Generated by Django 4.0.2 on 2022-08-23 23:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catgory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('descr', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
