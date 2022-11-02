# Generated by Django 4.1.3 on 2022-11-01 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guruapp', '0006_rename_town_shop_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='street',
            name='city',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='guruapp.city', verbose_name='город'),
            preserve_default=False,
        ),
    ]
