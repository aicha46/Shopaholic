# Generated by Django 2.0.13 on 2019-03-31 12:36

from django.db import migrations, models
import django.db.models.deletion
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderanditemcharges',
            options={'ordering': ['name'], 'verbose_name': 'Order and Item Charge', 'verbose_name_plural': 'Order and Item Charges'},
        ),
        migrations.AlterModelOptions(
            name='weightband',
            options={'ordering': ['method', 'upper_limit'], 'verbose_name': 'Weight Band', 'verbose_name_plural': 'Weight Bands'},
        ),
        migrations.AlterModelOptions(
            name='weightbased',
            options={'ordering': ['name'], 'verbose_name': 'Weight-based Shipping Method', 'verbose_name_plural': 'Weight-based Shipping Methods'},
        ),
        migrations.AlterField(
            model_name='orderanditemcharges',
            name='code',
            field=oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='orderanditemcharges',
            name='countries',
            field=models.ManyToManyField(blank=True, to='address.Country', verbose_name='Countries'),
        ),
        migrations.AlterField(
            model_name='weightband',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bands', to='shipping.WeightBased', verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='weightbased',
            name='code',
            field=oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='weightbased',
            name='countries',
            field=models.ManyToManyField(blank=True, to='address.Country', verbose_name='Countries'),
        ),
    ]
