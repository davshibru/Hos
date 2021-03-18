# Generated by Django 3.1.7 on 2021-03-18 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimesOfWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='время начала приема')),
                ('end_time', models.TimeField(verbose_name='время конца приема')),
            ],
            options={
                'verbose_name': 'Время работы',
                'verbose_name_plural': 'Время работы',
            },
        ),
    ]