# Generated by Django 3.2.7 on 2021-09-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('when', models.DateTimeField()),
                ('date', models.DateField()),
                ('start', models.CharField(max_length=20)),
                ('end', models.CharField(max_length=20)),
                ('discription', models.TextField()),
            ],
        ),
    ]
