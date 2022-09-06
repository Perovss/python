from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def main_page(request):
    msg = 'Расчет количества ингредиентов для блюд.'
    return HttpResponse(msg)


def recipes(request, dish):
    ingredients = DATA.get(dish)
    
    if ingredients:
        context = {'dish': dish, 'recipe': {}}
        try:
            persons = int(request.GET.get('servings', 1))
        except Exception as err:
            return HttpResponse(f'Ошибка: {err}')
        
        for name_ingredient, amount in ingredients.items():
            context['recipe'][name_ingredient] = amount * persons
    else:
        context = {'dish': ""}

        return render(request, 'calculator/index.html', context)

