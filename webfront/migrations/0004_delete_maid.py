# Generated by Django 2.2.7 on 2019-12-03 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_cart', '0002_auto_20191203_0605'),
        ('shortlisted_cart', '0002_auto_20191203_0605'),
        ('webfront', '0003_auto_20191129_0825'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Maid',
        ),
    ]