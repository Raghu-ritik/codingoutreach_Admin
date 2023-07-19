# Generated by Django 3.2.7 on 2021-12-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects1',
            fields=[
                ('projectid', models.AutoField(primary_key=True, serialize=False)),
                ('projectname', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('creator', models.CharField(max_length=50)),
                ('datecreated', models.DateTimeField()),
                ('purpose', models.CharField(max_length=250)),
                ('Availability', models.BooleanField()),
                ('Image', models.ImageField(upload_to='Projects1/images')),
                ('rating', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)])),
                ('introvideo', models.FileField(upload_to='Projects1/videos')),
            ],
        ),
    ]
