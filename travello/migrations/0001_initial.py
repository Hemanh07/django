# Generated by Django 5.0.2 on 2024-03-01 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinatiion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('offer', models.BooleanField(default=False)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
