# Generated by Django 3.2.7 on 2021-09-28 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_event'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='discription',
            new_name='description',
        ),
    ]
