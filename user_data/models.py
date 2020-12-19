from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Character(models.Model):
  char_elements = (
  (1,"火"),
  (2,"水"),
  (3,"木"),
  (4,"光"),
  (5,"闇"),
  )
  char_stars = (
    (1,"☆☆☆"),
    (2,"☆☆☆☆"),
    (3,"☆☆☆☆☆"),
    (4,"☆☆☆☆☆☆"),
  )
  character_name = models.CharField(max_length=30)
  element = models.SmallIntegerField(choices=char_elements)
  Stars = models.SmallIntegerField(choices=char_stars)
  Level = models.SmallIntegerField(default=1)
  Favorability_rating = models.SmallIntegerField(default=1)
  add_date = models.DateTimeField(default=timezone.now)
  mod_date = models.DateTimeField(default=timezone.now)

class Equipment(models.Model):
  level_ranks = (
    (1,'under85'),
    (2,'85'),
    (3,'88'),
    (4,'90'),
  )
  rare_ranks = (
    (1,'エピック'),
    (2,'レジェンド'),
    (3,'レア'),
  )
  equip_parts = (
    (1, "武器"),
    (2, "頭"),
    (3, "体"),
    (4, "首"),
    (5, "指"),
    (6, "足"),
  )
  set_options = (
    (1,"憤怒"),
    (2,"免疫"),
    (3,"連携"),
    (4,"反撃"),
    (5,"吸収"),
    (6,"破滅"),
    (7,"速度"),
    (8,"抵抗"),
    (9,"命中"),
    (10,"会心"),
    (11,"生命"),
    (12,"攻撃"),
    (13,"防御"),
  )
  Level = models.PositiveSmallIntegerField(choices=level_ranks,default=2)
  S_Level = models.PositiveSmallIntegerField(default=15)
  rare_rank = models.PositiveSmallIntegerField(choices=rare_ranks,default=1)
  Part = models.PositiveSmallIntegerField(choices=equip_parts)
  set_option = models.PositiveSmallIntegerField(choices=set_options,default=7)
  atk = models.PositiveSmallIntegerField(blank=True,null=True)
  atk_rate = models.PositiveSmallIntegerField(blank=True,null=True)
  defence = models.PositiveSmallIntegerField(blank=True,null=True)
  defence_rate = models.PositiveSmallIntegerField(blank=True,null=True)
  hp = models.PositiveSmallIntegerField(blank=True,null=True)
  hp_rate = models.PositiveSmallIntegerField(blank=True,null=True)
  res = models.PositiveSmallIntegerField(blank=True,null=True)
  hit = models.PositiveSmallIntegerField(blank=True,null=True)
  cri_dmg = models.PositiveSmallIntegerField(blank=True,null=True)
  cri_rate = models.PositiveSmallIntegerField(blank=True,null=True)
  speed = models.PositiveSmallIntegerField(blank=True,null=True)
  add_date = models.DateTimeField(default=timezone.now)
  mod_date = models.DateTimeField(default=timezone.now)
