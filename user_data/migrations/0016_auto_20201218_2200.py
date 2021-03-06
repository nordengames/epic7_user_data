# Generated by Django 3.1.4 on 2020-12-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0015_auto_20201218_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='Level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'under85'), (2, '85'), (3, '88'), (4, '90')], default=2),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='S_Level',
            field=models.PositiveSmallIntegerField(default=15),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='set_option',
            field=models.PositiveSmallIntegerField(choices=[(1, '憤怒'), (2, '免疫'), (3, '連携'), (4, '反撃'), (5, '吸収'), (6, '破滅'), (7, '速度'), (8, '抵抗'), (9, '命中'), (10, '会心'), (11, '生命'), (12, '攻撃')], default=7),
        ),
    ]
