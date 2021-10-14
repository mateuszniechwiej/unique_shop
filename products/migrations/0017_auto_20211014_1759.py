# Generated by Django 3.2.7 on 2021-10-14 16:59

import cloudinary.models
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_colour_colour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
        migrations.RemoveField(
            model_name='size',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_diff_colors',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_more_images',
        ),
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='colors',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('red', 'RED'), ('yellow', 'YELLOW'), ('blue', 'BLUE'), ('orange', 'ORANGE'), ('green', 'GREEN'), ('black', 'BLACK')], max_length=34, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='Colour',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
    ]
