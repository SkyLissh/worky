# Generated by Django 4.0.5 on 2022-06-12 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skills',
            new_name='Skill',
        ),
    ]