# Generated by Django 5.0 on 2024-01-05 14:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprecipe', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='recipe',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Рецепт'),
        ),
    ]
