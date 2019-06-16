# Generated by Django 2.2 on 2019-06-16 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20190616_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country1',
            fields=[
                ('name', models.CharField(max_length=250, primary_key=True, serialize=False, unique=True)),
                ('flag', models.ImageField(blank=True, null=True, upload_to='')),
                ('shortname', models.CharField(max_length=256, unique=True)),
                ('description', models.TextField(default='about your country', max_length=555)),
            ],
        ),
    ]
