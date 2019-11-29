# Generated by Django 2.2.7 on 2019-11-28 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webfront', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=20)),
                ('type_of_maid', models.CharField(max_length=20)),
                ('agency_name', models.CharField(max_length=50)),
                ('maid_photo', models.ImageField(default=None, upload_to='images/maidphoto')),
            ],
        ),
        migrations.DeleteModel(
            name='Searchmaid',
        ),
    ]
