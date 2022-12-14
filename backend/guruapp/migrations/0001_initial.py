# Generated by Django 4.1.3 on 2022-11-01 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='обьект создан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='обьект изменен')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='обьект создан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='обьект изменен')),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='обьект создан')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='обьект изменен')),
                ('house', models.CharField(max_length=150)),
                ('time_open', models.DateTimeField()),
                ('time_closed', models.DateTimeField()),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruapp.street', verbose_name='Улица')),
                ('town', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guruapp.town', verbose_name='Город')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
