import random, os, platform
from choices import Choices


"""
    Brief: Cette fonction crée un lieu aléatoire sous forme de string
           compatible avec le type Geometry de Mysql.
    Arg[boundaries]: La région de lieu possible est un rectangle de coin
                     inférieur gauche (0,0) et de coin supérieur droit boundaries.
                     Boundaries est donc un tuple de deux entiers.
"""
def create_location(boundaries):
    lat = round(random.uniform(0, boundaries[1]), 3)
    lon = round(random.uniform(0, boundaries[0]), 3)
    if lat == int(lat): lat += 0.001
    if lon == int(lon): lon += 0.001
    return '"POINT({} {})"'.format(lat, lon)


"""
    Brief: Cette fonction génère les tuples de catégories de supports
           à partir des données définies dans le module choices.
    Arg[graph]: Une instance de Graph pour lequel on veut insérer ces tuples.
"""
def gen_categories_supports(graph):
    for c in Choices.supports:
        graph.tuples["CATEGORIESDESUPPORTS"].append(c)





"""
    Brief: Cette fonction permet d'afficher une barre de chargement.
    Arg[text]: String indiquant ce qui est chargé.
    Arg[loading_ratio]: Float entre 0 et 1 indiquant l'avancement du chargement.
"""
def display_loading(text, loading_ratio):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    bar_length = 40
    loaded = int(loading_ratio * bar_length)
    bar = '|' * loaded  + '-' * (bar_length - loaded) 
    print("{0}   {1}    {2:3.2f}%".format(text, bar, loading_ratio*100))


"""
    Brief: Cette fonction permet de découvrir le plus grand diviseur d'un nombre
           donné et l'autre diviseur associé à celui-ci. Par exemple, pour 12,
           la fonction retournerait (6, 2).
    Arg[n]: Le nombre qu'on veut décomposer.
    Return: Un tuple de deux entiers.
"""
def get_divisors(n):
    original_n = n
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    max_factor = max(factors)
    return max_factor, original_n // max_factor

