from django.contrib import admin

# Register your models here.
from .models import Character
from .models import Equipment

class CharacterAdmin(admin.ModelAdmin):
  list_display = ('character_name', 'element', 'Stars', 'Level',)
  list_display_links = ('character_name', 'element', 'Stars', 'Level',)

class EquipmentAdmin(admin.ModelAdmin):
  list_display = ('Level',)
  list_display_links = ('Level',)

admin.site.register(Character, CharacterAdmin)
admin.site.register(Equipment, EquipmentAdmin )