# Generated by Django 3.2.7 on 2023-07-30 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0005_remove_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='categoryF',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.categoryfield', verbose_name='Category'),
        ),
    ]
