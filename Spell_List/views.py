from django.shortcuts import render, render_to_response, get_list_or_404
from Spell_List.models import Spell


def index(request):
    return render_to_response("Spell_List/index.html", {
        "spells": get_list_or_404(Spell.objects.all())
    })
