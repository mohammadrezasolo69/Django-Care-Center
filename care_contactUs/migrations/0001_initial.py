# Generated by Django 4.0.2 on 2022-02-22 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_1', models.CharField(max_length=12)),
                ('phone_2', models.CharField(max_length=12)),
                ('phone_3', models.CharField(max_length=12)),
            ],
        ),
    ]