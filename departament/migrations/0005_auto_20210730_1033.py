# Generated by Django 3.2.5 on 2021-07-30 06:33

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('departament', '0004_auto_20210729_1249'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departament',
            options={'ordering': ['name'], 'verbose_name': 'Şöbə', 'verbose_name_plural': 'Şöbələr'},
        ),
        migrations.AlterModelOptions(
            name='departamentschedule',
            options={'verbose_name': 'Şöbə İş Rejmi', 'verbose_name_plural': 'Şöbə İş Rejimləri'},
        ),
        migrations.AlterField(
            model_name='departament',
            name='about',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Haqqında Məlumat'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma Tarixi'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='description',
            field=models.TextField(verbose_name='Qısa Məlumat'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='icon',
            field=imagekit.models.fields.ProcessedImageField(upload_to='departament/icons/', verbose_name='İkon'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Şöbə adı'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departament.departamentschedule', verbose_name='İş Rejmi'),
        ),
        migrations.AlterField(
            model_name='departament',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Son Dəyişdirilmə Tarixi'),
        ),
        migrations.AlterField(
            model_name='departamentimage',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma Tarixi'),
        ),
        migrations.AlterField(
            model_name='departamentimage',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='departament/images/', verbose_name='Şəkil Faylı'),
        ),
        migrations.AlterField(
            model_name='departamentimage',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlıq'),
        ),
        migrations.AlterField(
            model_name='departamentimage',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Son Dəyişdirilmə Tarixi'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma Tarixi'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='friday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Cümə Bitiş'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='friday_show',
            field=models.BooleanField(default=True, verbose_name='Cümə Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='friday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Cümə Başlanğıc'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='monday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Bazar Ertəsi Bitmə'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='monday_show',
            field=models.BooleanField(default=True, verbose_name='Bazar Ertəsi Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='monday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Bazar Ertəsi Başlanğıc'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='saturday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Şənbə Bitiş'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='saturday_show',
            field=models.BooleanField(default=True, verbose_name='Şənbə Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='saturday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Şənbə Başlanğıc'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='show_schedule',
            field=models.BooleanField(default=True, verbose_name='İş rejmini Saytda Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='sunday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Bazar Bitiş'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='sunday_show',
            field=models.BooleanField(default=False, verbose_name='Bazar Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='sunday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Bazar Başlanğıc'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='thursday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Cümə Axşamı Bitiş'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='thursday_show',
            field=models.BooleanField(default=True, verbose_name='Cümə Axşamı Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='thursday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Cümə Axşamı Başlanğıc'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Iş Rejmi Adı'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='tuesday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Çəşənbə Axşamı Bitiş'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='tuesday_show',
            field=models.BooleanField(default=True, verbose_name='Çərşənbə Axşamı Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='tuesday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Çərşənbə Axşamı Başlanğıc'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Son Dəyişdirilmə Tarixi'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='wednesday_end',
            field=models.TimeField(default=datetime.time(17, 0), verbose_name='Çəşənbə Bitiş'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='wednesday_show',
            field=models.BooleanField(default=True, verbose_name='Çəşənbə Rejmi Göstərilsin'),
        ),
        migrations.AlterField(
            model_name='departamentschedule',
            name='wednesday_start',
            field=models.TimeField(default=datetime.time(9, 0), verbose_name='Çəşənbə Başlanğıc'),
        ),
    ]
