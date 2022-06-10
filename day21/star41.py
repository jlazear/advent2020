from collections import Counter

def make_ingredients_dict(recipes):
    allergy_dict = {}
    for recipe in recipes:
        ingredients = recipe[0]
        allergens = recipe[1]
        for allergen in allergens:
            if allergen in allergy_dict:
                allergy_dict[allergen] = allergy_dict[allergen].intersection(ingredients)
            else:
                allergy_dict[allergen] = ingredients
    return allergy_dict


recipes = []
all_ingredients = Counter()
all_allergens = Counter()
for line in open('input.txt'):
    ingredients_str, allergens_str = line.split('(')
    ingredients = set(ingredients_str.strip().split())
    allergens = set(allergens_str[9:].strip(' )\n').split(', '))
    recipes.append((ingredients, allergens))
    all_ingredients.update(ingredients)
    all_allergens.update(allergens)
     
d = make_ingredients_dict(recipes)
allergen_dict = {}  # allergen: ingredient

i = 0
while d:
    i += 1
    if i > 10: break
    keys_to_pop = []
    remove_ingredients = set()
    for allergen, ingredients in d.items():
        if len(ingredients) == 1:
            ingredient = ingredients.pop()
            allergen_dict[allergen] = ingredient
            keys_to_pop.append(allergen)
            remove_ingredients.add(ingredient)
    
    for key in keys_to_pop:
        d.pop(key, None)
    
    for ingredient in remove_ingredients:
        for allergen, ingredients in d.items():
            ingredients.discard(ingredient)

for ingredient in allergen_dict.values():
    del all_ingredients[ingredient]

print('RESULTS:', sum(all_ingredients.values()))
