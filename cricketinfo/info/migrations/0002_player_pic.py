# Generated by Django 2.1.5 on 2019-06-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
