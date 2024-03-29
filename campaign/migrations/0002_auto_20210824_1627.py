# Generated by Django 3.2.5 on 2021-08-24 12:27

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='second_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='campaign/second/'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='third_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='campaign/third/'),
        ),
    ]
