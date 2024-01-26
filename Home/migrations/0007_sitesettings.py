# Generated by Django 3.2.7 on 2023-09-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20230729_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SiteName', models.CharField(default='CodingOutReach', max_length=100)),
                ('SiteHeadSLogan', models.CharField(default="Coding smith's on move", max_length=500)),
                ('SiteUrl', models.CharField(default='www.codingoutrach.com', max_length=200)),
                ('contactusEmail', models.EmailField(default='coonnect@codingoutreach.com', max_length=254)),
                ('adminEmail', models.EmailField(default='admin@codingoutreach.com', max_length=254)),
                ('usersCanRegister', models.BooleanField(default=True, null=True)),
                ('ProjectsAvailable', models.BooleanField(default=False, null=True)),
                ('ProductsAvailable', models.BooleanField(default=False, null=True)),
                ('LearnWithUsAvailable', models.BooleanField(default=False, null=True)),
                ('NotesAvailable', models.BooleanField(default=False, null=True)),
                ('SiteLogo', models.ImageField(blank=True, default='', null=True, upload_to='siteMedia/SiteLogo')),
                ('updatedOn', models.DateTimeField(auto_now_add=True, null=True)),
                ('BannerImg1', models.ImageField(blank=True, default='', null=True, upload_to='siteMedia\\SiteBanner')),
                ('BannerImg2', models.ImageField(blank=True, default='', null=True, upload_to='siteMedia\\SiteBanner')),
                ('BannerImg3', models.ImageField(blank=True, default='', null=True, upload_to='siteMedia\\SiteBanner')),
                ('BannerImg4', models.ImageField(blank=True, default='', null=True, upload_to='siteMedia\\SiteBanner')),
                ('NewsApiURL', models.CharField(blank=True, max_length=200, null=True)),
                ('NewAPIToken', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Site Settings',
                'verbose_name_plural': 'Site Setings',
            },
        ),
    ]