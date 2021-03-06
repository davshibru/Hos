# Generated by Django 3.1.6 on 2021-02-16 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилие')),
                ('position', models.CharField(max_length=200, verbose_name='Должность')),
                ('info', models.CharField(max_length=1000, verbose_name='Информация о пользователе')),
            ],
            options={
                'verbose_name': 'Врач',
                'verbose_name_plural': 'Врачи',
            },
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата приема')),
                ('time', models.TimeField(verbose_name='время приема')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('patient_info', models.CharField(max_length=1000, verbose_name='Информация о поциенте')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.doctors', verbose_name='Доктор')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Прием',
                'verbose_name_plural': 'Приемы',
            },
        ),
    ]
