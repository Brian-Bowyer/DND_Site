from django.shortcuts import render, render_to_response
from Spell_List.models import Spell

#TODO: Make views
def index(request):
    spells = Spell.objects.all()
    return render_to_response('Spell_List/index.html', context=spells)