# Generated by Django 3.1.4 on 2020-12-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0014_auto_20201218_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='Level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'under85'), (2, '85'), (3, '88'), (4, '90')]),
        ),
    ]
