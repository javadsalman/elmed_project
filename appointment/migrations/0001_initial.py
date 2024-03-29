# Generated by Django 3.2.5 on 2021-07-28 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('day', models.DateField()),
                ('time', models.TimeField()),
                ('note', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='departament.departament')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]
