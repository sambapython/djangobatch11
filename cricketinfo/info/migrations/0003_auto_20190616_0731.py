# Generated by Django 2.2 on 2019-06-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20190616_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='shortname',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]