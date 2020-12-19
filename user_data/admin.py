from django.contrib import admin

# Register your models here.
from .models import Character
from .models import Equipment

class CharacterAdmin(admin.ModelAdmin):
  list_display = ('character_name', 'element', 'Stars', 'Level',)
  list_display_links = ('character_name', 'element', 'Stars', 'Level',)

class EquipmentAdmin(admin.ModelAdmin):
  list_display= ('Level','S_Level','rare_rank', 'Part', 'set_option','atk','atk_rate', 'defence', 'defence_rate', 'hp', 'hp_rate', 'res', 'hit', 'cri_dmg', 'cri_rate', 'speed')
  list_filter = ['Part','Level','rare_rank','set_option']

admin.site.register(Character, CharacterAdmin)
admin.site.register(Equipment, EquipmentAdmin )