# Generated by Django 3.2.3 on 2023-11-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
