# Generated by Django 4.0.2 on 2022-02-22 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_gallery', '0005_alter_imggallery_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='care_gallery.gallery'),
        ),
    ]