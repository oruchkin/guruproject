# Generated by Django 4.1.3 on 2022-11-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guruapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='qtitle',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]