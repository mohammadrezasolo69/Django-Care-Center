# Generated by Django 4.0.2 on 2022-02-22 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care_gallery', '0013_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]
