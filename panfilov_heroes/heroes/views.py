from fuzzywuzzy import fuzz
from django.shortcuts import render
from .models import Hero

def hero_search(request):
    query = request.GET.get('q')
    heroes = []
    if query:
        all_heroes = Hero.objects.all()
        for hero in all_heroes:
            similarity_last_name = fuzz.partial_ratio(hero.last_name.lower(), query.lower())
            similarity_first_name = fuzz.partial_ratio(hero.first_name.lower(), query.lower())
            similarity_patronymic = fuzz.partial_ratio(hero.patronymic.lower(), query.lower())

            if similarity_last_name > 70 or similarity_first_name > 70 or similarity_patronymic > 70:
                heroes.append(hero)

        return render(request, 'heroes/results.html', {'heroes': heroes, 'query': query})
    return render(request, 'heroes/search.html', {'heroes': heroes, 'query': query})
