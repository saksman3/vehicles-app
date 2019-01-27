# Generated by Django 2.1 on 2018-11-02 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partsorderlist',
            old_name='bookingID',
            new_name='serialNumber',
        ),
        migrations.AlterField(
            model_name='servicebookings',
            name='serviceType',
            field=models.CharField(choices=[('MAJOR', 'major'), ('NORMAL', 'normal'), ('minor', 'MINOR')], default='Normal', max_length=255),
        ),
    ]
