# Generated by Django 5.0.2 on 2024-03-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinatiion',
            name='desc',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='destinatiion',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
