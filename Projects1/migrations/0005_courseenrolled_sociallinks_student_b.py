# Generated by Django 3.2.7 on 2022-01-06 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Projects1', '0004_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_B',
            fields=[
                ('studid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('basiverification', models.BooleanField(default=False)),
                ('majorverified', models.BooleanField(default=False)),
                ('profile_pic', models.ImageField(blank=True, default='profile1.png', null=True, upload_to='Users/stud_B/')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('colid', models.ImageField(blank=True, default='', null=True, upload_to='Users/stud_B/')),
                ('User', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('SIid', models.AutoField(primary_key=True, serialize=False)),
                ('Github', models.CharField(blank=True, max_length=200, null=True)),
                ('Medium', models.CharField(blank=True, max_length=200, null=True)),
                ('Linkedin', models.CharField(blank=True, max_length=200, null=True)),
                ('filled', models.BooleanField(default=False)),
                ('profileId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Courseenrolled',
            fields=[
                ('CEid', models.AutoField(primary_key=True, serialize=False)),
                ('courseid', models.ManyToManyField(blank=True, to='Projects1.Projects1')),
                ('profileId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
