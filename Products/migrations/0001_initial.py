# Generated by Django 3.2.7 on 2022-07-28 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productid', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Web development', 'Web development'), ('Machine Learning', 'Machine Learning'), ('Data Science', 'Data Science'), ('PHP', 'PHP'), ('C/C++', 'C/C++'), ('Others', 'Others')], max_length=35, null=True)),
                ('desc', models.CharField(max_length=500)),
                ('creator', models.CharField(max_length=50)),
                ('datecreated', models.DateTimeField()),
                ('purpose', models.CharField(max_length=250)),
                ('Availability', models.BooleanField()),
                ('Image', models.ImageField(upload_to='Pproducts/images')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('introvideo', models.FileField(upload_to='Pproducts/videos')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('Contentid', models.AutoField(primary_key=True, serialize=False)),
                ('filename', models.CharField(max_length=50)),
                ('fileup', models.FileField(upload_to='Products/filesup/')),
                ('coverup', models.ImageField(upload_to='Products/covers/')),
                ('projasso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Products.products')),
            ],
        ),
    ]
