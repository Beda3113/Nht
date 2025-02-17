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
    # можете добавить свои рецепты ;)
}

def recipe(request, dish):  
    if dish in DATA:
        recipe_data = DATA[dish].copy()     
        servings = request.GET.get('servings')
        if servings:
            try:
                servings = int(servings)
                for ingredient, amount in recipe_data.items():
                    recipe_data[ingredient] = amount * servings
            except ValueError:
                pass
        context = {
            'recipe': recipe_data
        }

        # Рендерим шаблон с контекстом
        return render(request, 'calculator/index.html', context)
    else:
        # Если блюдо не найдено, возвращаем 404
        return render(request, '404.html', status=404)
