# Generated by Django 3.2.5 on 2021-08-02 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departament', '0005_auto_20210730_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamentimage',
            name='title',
        ),
    ]
