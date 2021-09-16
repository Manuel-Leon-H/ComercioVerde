# Generated by Django 3.2.7 on 2021-09-10 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0003_auto_20210909_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artesanias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreArtesania', models.CharField(blank=True, max_length=100, null=True)),
                ('PrecioArtesania', models.FloatField(blank=True, max_length=7, null=True)),
                ('FotoArtesania', models.ImageField(blank=True, null=True, upload_to='')),
                ('RegionArtesania', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
