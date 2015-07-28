from django.db import models

class Component(models.Model):
    name = models.CharField(max_length = 255, default = "")
    abbreviation = models.CharField(max_length = 5, default = "")

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length = 255)

    is_ritual = models.BooleanField(default = False)
    is_concentration = models.BooleanField(default = False)

    level = models.PositiveSmallIntegerField(default = 0)

    school = models.CharField(max_length = 255, default= "")
    casting_time = models.CharField(max_length = 255, default= "1 action") #TODO: Make a DNDTime model
    duration = models.CharField(max_length = 255, default= "", blank=True)
    range = models.CharField(max_length = 255, default="", blank= True)

    description = models.TextField(default="")
    at_higher_levels = models.TextField(default="", blank=True)

    components = models.ManyToManyField(Component)
    #TODO: Add secondary attributes damage, damage type, scaling

    def __str__(self):
        return self.name

class CharacterClass(models.Model):
    name = models.CharField(max_length = 255, default = "")
    canCast = models.ManyToManyField(Spell)

    def __str__(self):
        return self.name