# Generated by Django 3.2.7 on 2023-07-29 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20230725_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='projectsenrolled',
            options={'verbose_name': 'Project Enrolled Users', 'verbose_name_plural': 'Project Enrolled Users'},
        ),
        migrations.AlterModelOptions(
            name='sociallinks',
            options={'verbose_name': 'Social Links', 'verbose_name_plural': 'Social Links'},
        ),
        migrations.AlterModelOptions(
            name='student_b',
            options={'verbose_name': 'Users Info', 'verbose_name_plural': 'Users Info'},
        ),
    ]
