# Generated by Django 3.2.7 on 2023-07-29 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LearnWithUS', '0002_auto_20230725_2313'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learnmodel',
            options={'verbose_name': 'Learning Module', 'verbose_name_plural': 'Learning Module'},
        ),
        migrations.AlterModelOptions(
            name='notesfile',
            options={'verbose_name': 'Learning Module Notes', 'verbose_name_plural': 'Learning Module Notes'},
        ),
    ]