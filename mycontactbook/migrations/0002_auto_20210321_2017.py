# Generated by Django 3.1.6 on 2021-03-21 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycontactbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcontact',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
