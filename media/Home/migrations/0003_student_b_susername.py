# Generated by Django 3.2.7 on 2022-01-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_courseenrolled_sociallinks_student_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_b',
            name='Susername',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]