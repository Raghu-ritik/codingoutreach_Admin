# Generated by Django 3.2.7 on 2022-01-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_student_b_susername'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_b',
            name='mobno',
            field=models.IntegerField(null=True),
        ),
    ]