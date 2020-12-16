from django.contrib import admin

# Register your models here.
from .models import Character

class CharacterAdmin(admin.ModelAdmin):
  list_display = ('character_name', 'element', 'Stars', 'Level',)
  list_display_links = ('character_name', 'element', 'Stars', 'Level',)

admin.site.register(Character, CharacterAdmin)