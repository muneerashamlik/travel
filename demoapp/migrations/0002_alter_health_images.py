# Generated by Django 5.0.1 on 2024-02-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health',
            name='images',
            field=models.ImageField(upload_to='pictures'),
        ),
    ]
