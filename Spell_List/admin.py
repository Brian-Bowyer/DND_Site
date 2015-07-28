from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'school', 'casting_time', 'duration', 'range', 'is_ritual', 'is_concentration')

@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'name')

@admin.register(CharacterClass)
class CharacterClassAdmin(admin.ModelAdmin):
    pass