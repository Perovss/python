# Generated by Django 4.1 on 2022-10-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]