# Generated by Django 3.1.4 on 2020-12-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_data', '0013_equipment_set_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='S_Level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'under85'), (2, '85'), (3, '90')]),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Part',
            field=models.PositiveSmallIntegerField(choices=[(1, '武器'), (2, '頭'), (3, '体'), (4, '首'), (5, '指'), (6, '足')]),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='atk',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='atk_rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cri_dmg',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='cri_rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='defence',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='defence_rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='hit',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='hp',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='hp_rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='rare_rank',
            field=models.PositiveSmallIntegerField(choices=[(1, 'エピック'), (2, 'レジェンド'), (3, 'レア')], default=1),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='res',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='set_option',
            field=models.PositiveSmallIntegerField(choices=[(1, '憤怒'), (2, '免疫'), (3, '連携'), (4, '反撃'), (5, '吸収'), (6, '破滅'), (7, '速度'), (8, '抵抗'), (9, '命中'), (10, '会心'), (11, '生命'), (12, '攻撃')], default=1),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='speed',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]