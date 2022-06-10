from star41 import *

sorted_dangerous = sorted([(allergen, ingredient) for allergen, ingredient in allergen_dict.items()], key=lambda x: x[0])

from_star41_import_solution = ','.join([ingredient for allergen, ingredient in sorted_dangerous])

print(from_star41_import_solution)