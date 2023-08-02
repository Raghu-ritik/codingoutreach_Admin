# Generated by Django 3.2.7 on 2023-07-29 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Products', '0002_auto_20230725_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'verbose_name': 'Product Conent', 'verbose_name_plural': 'Product Conent'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Site Products', 'verbose_name_plural': 'Site Products'},
        ),
        migrations.CreateModel(
            name='ProductsEnrolledUser',
            fields=[
                ('CEid', models.AutoField(primary_key=True, serialize=False)),
                ('productid', models.ManyToManyField(blank=True, to='Products.Products', verbose_name='Courses Enrolled ID')),
                ('profileId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User ID')),
            ],
            options={
                'verbose_name': 'Product Enrolled Users',
                'verbose_name_plural': 'Product Enrolled Users',
            },
        ),
    ]