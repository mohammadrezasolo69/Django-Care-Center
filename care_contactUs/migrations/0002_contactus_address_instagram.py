# Generated by Django 4.0.2 on 2022-02-22 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care_contactUs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='address_instagram',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
