# Generated by Django 2.2.4 on 2019-11-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Searchmaid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('nationality', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('marital_status', models.CharField(max_length=20)),
                ('type_of_maid', models.CharField(max_length=20)),
                ('agency_name', models.CharField(max_length=50)),
            ],
        ),
    ]
