from django.shortcuts import render
from .models import Skills
from personages.models import Personage

def index(request):
    # all_animals = Animal.objects.prefetch_related('animalfood_set').all()  # python level
    all_stats = Skills.objects.all()

    context = {
        'all_stats': all_stats,
    }

    return render(request, 'index.html', context=context)
