# Generated by Django 2.2.7 on 2019-11-28 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency_user',
            name='person_in_charge',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]