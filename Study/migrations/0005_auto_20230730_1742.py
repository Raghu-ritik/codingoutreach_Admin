# Generated by Django 3.2.7 on 2023-07-30 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Study', '0004_auto_20230729_2143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branchfornotes',
            options={'verbose_name': 'Branch', 'verbose_name_plural': 'Branch'},
        ),
        migrations.AlterModelOptions(
            name='categoryofnotes',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='coursefor',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='semeserfornotes',
            options={'verbose_name': 'Semester', 'verbose_name_plural': 'Semester'},
        ),
        migrations.AlterModelOptions(
            name='subjectofnotes',
            options={'verbose_name': 'Subject', 'verbose_name_plural': 'Subject'},
        ),
        migrations.AlterField(
            model_name='notes1',
            name='branch',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Study.semeserfornotes', verbose_name='Branch'),
        ),
        migrations.AlterField(
            model_name='notes1',
            name='category',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Study.categoryofnotes', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='notes1',
            name='coursefor',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Study.coursefor', verbose_name='Course Stream'),
        ),
        migrations.AlterField(
            model_name='notes1',
            name='semeter',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Study.branchfornotes', verbose_name='Semester'),
        ),
        migrations.AlterField(
            model_name='notes1',
            name='subject',
            field=models.ForeignKey(blank=True, max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Study.subjectofnotes', verbose_name='Subject'),
        ),
    ]
