# Generated by Django 2.2.7 on 2019-12-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20191206_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='enquiry',
            name='age',
            field=models.CharField(choices=[('23 to 25', '23 to 25'), ('26 to 30', '26 to 30'), ('31 to 35', '31 to 35'), ('36 to 40', '36 to 40'), ('41 to 50', '41 to 50'), ('No Preference', 'No Preference')], default='No Preference', max_length=50),
        ),
        migrations.AddField(
            model_name='enquiry',
            name='type_of_maid',
            field=models.CharField(choices=[('New', 'New'), ('Transfer', 'Transfer'), ('Experience', 'Experience'), ('No Preference', 'No Preference')], default='No Preference', max_length=50),
        ),
    ]
