# Generated by Django 3.2.5 on 2021-07-29 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_articlimage_articleimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Kateqoriya', 'verbose_name_plural': 'Kateqoriyalar'},
        ),
        migrations.RenameField(
            model_name='articleimage',
            old_name='image_file',
            new_name='image',
        ),
    ]
