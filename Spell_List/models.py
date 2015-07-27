from django.db import models

class Spell(models.Model):
    name = models.CharField(max_length=255)
    is_ritual = models.BooleanField(default=False)
    is_concentration = models.BooleanField(default=False)
    level = models.PositiveSmallIntegerField(default=0)
    school = models.CharField(max_length=255)
    casting_time = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description = models.TextField()

    components = models.ManyToManyField(Component)
    canBeCastBy = models.ManyToManyField(CharacterClass)

class Component(models.Model):
    pass

class CharacterClass(models.Model):
    pass