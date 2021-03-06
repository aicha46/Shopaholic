# Generated by Django 2.0.13 on 2019-04-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0011_remove_service_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='tel',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='ville',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='wilaya',
            field=models.CharField(blank=True, choices=[('oran', 'oran'), ('alger', 'alger')], max_length=255, null=True),
        ),
    ]
