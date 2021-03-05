# Generated by Django 3.1.7 on 2021-03-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0002_crop_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='crops')),
            ],
        ),
        migrations.AddField(
            model_name='crop',
            name='land_type',
            field=models.CharField(choices=[('chalk soil', 'chalk soil'), ('clay soil', 'clay soil'), ('loam soil', 'loam soil'), ('peat soil', 'peat soil'), ('sandy soil', 'sandy soil'), ('silt soil', 'silt soil')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
