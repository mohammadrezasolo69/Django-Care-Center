# Generated by Django 4.0.2 on 2022-02-21 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_gallery', '0004_remove_gallery_count_img_alter_imggallery_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imggallery',
            name='gallery',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='care_gallery.gallery'),
        ),
    ]
