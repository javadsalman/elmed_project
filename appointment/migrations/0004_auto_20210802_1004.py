# Generated by Django 3.2.5 on 2021-08-02 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20210730_1033'),
        ('departament', '0006_remove_departamentimage_title'),
        ('appointment', '0003_auto_20210730_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='departament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='departament.departament', verbose_name='Müraciət Edilən Şöbə'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctor', verbose_name='Müraciət Edilən Həkim'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, verbose_name='Email Ünvanı'),
        ),
    ]
