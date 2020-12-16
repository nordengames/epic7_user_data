from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Character(models.Model):
  character_name = models.CharField(max_length=30)
  element = models.CharField(max_length=10)
  Stars = models.SmallIntegerField(default=3)
  Level = models.SmallIntegerField(default=1)
  Favorability_rating = models.SmallIntegerField(default=1)
  add_date = models.DateTimeField(default=timezone.now)
  mod_date = models.DateTimeField(default=timezone.now)