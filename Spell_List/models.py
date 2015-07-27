from django.db import models

class Component(models.Model):
    #TODO: Fill out Component model
    pass

class CharacterClass(models.Model):
    #TODO: Fill out CharacterClass model
    pass

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

