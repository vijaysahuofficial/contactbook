# Generated by Django 3.1.6 on 2021-03-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycontactbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcontact',
            name='company',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='addcontact',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]