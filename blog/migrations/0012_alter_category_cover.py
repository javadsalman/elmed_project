# Generated by Django 3.2.5 on 2021-08-20 07:44

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_category_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category/cover/', verbose_name='Qapaq Şəkli'),
        ),
    ]