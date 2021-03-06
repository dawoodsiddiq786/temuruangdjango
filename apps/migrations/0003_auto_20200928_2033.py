# Generated by Django 2.2.12 on 2020-09-28 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_auto_20200928_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='duration',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='activity',
            name='overview',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='activity',
            name='supplier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suplier_user', to='apps.User'),
        ),
        migrations.AddField(
            model_name='activity',
            name='tags',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='unit_name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ImageField(upload_to='media'),
        ),
    ]
