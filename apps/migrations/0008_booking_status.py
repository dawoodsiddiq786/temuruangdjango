# Generated by Django 2.2.12 on 2020-10-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_auto_20201003_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
