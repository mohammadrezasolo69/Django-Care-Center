# Generated by Django 4.0.2 on 2022-02-22 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_gallery', '0015_alter_subcategory_sub_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('img', models.ImageField(upload_to='gallery/')),
                ('status', models.BooleanField(default=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images_gallery', to='care_gallery.gallery')),
            ],
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
