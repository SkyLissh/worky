# Generated by Django 4.0.5 on 2022-06-08 03:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('short_name', models.CharField(max_length=20, verbose_name='Short name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
        ),
    ]
