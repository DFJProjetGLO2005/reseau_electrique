import random
import pickle
import util

"""
    Brief: Cette classe se charge de créer une séries de villes contigues géographiquement. 
"""
class CityGenerator:
    """
        Brief: La construction de la classe est suffisante pour générer toutes les villes
               et les enregistrer en fichier csv.
    """
    def __init__(self):
        self.load_city_names()
        self.cities = []
        self.generate_cities()
        self.create_csv_file()
            

    """
        Brief: Cette fonction se charge de générer toutes les villes
               en leur donnant des dimensions aléatoires. Elle s'assure
               cependant qu'elles soient toutes contigues et que la
               région résultante sera rectangulaire.
    """
    def generate_cities(self):
        vertical_qty, horizontal_qty = util.get_divisors(len(self.names))
        lat = 0
        for y in range(vertical_qty):
            lon = 0
            height = random.randint(2, 20)
            for x in range(horizontal_qty):
                width = 10
                self.generate_one_city(lon, lat, width, height)
                lon += width
            lat += height
        self.boundaries = lat, lon


    """
        Brief: Cette fonction se charge de créer une ville et de lui
               donner un nom.
        Arg[lon]: La longitude du coin bas gauche du rectangle constituant cette ville
        Arg[lat]: La latitude du coin bas gauche du rectangle constituant cette ville
        Arg[width]: La largeur du rectangle constituant cette ville
        Arg[height]: La hauteur du rectangle constituant cette ville
    """
    def generate_one_city(self, lon, lat, width, height): 
        name = self.choose_name()
        self.cities.append([name,
                            'POLYGON(({} {}, {} {}, {} {}, {} {}, {} {}))'.format(
                            lon, lat,
                            lon + width, lat,
                            lon + width, lat + height,
                            lon, lat + height,
                            lon, lat)])

    """
        Brief: Cette fonction choisit un nom de ville aléatoirement.
        Return: Le nom de ville choisi
    """
    def choose_name(self):
        name = random.choice(self.names)
        self.names.remove(name)
        return name

    """
        Brief: Cette fonction charge tous les noms de villes possibles
               conservés dans le fichier binaire data/cities.pkl
    """
    def load_city_names(self):
        f = open("data/cities.pkl", 'rb')
        self.names = pickle.load(f)
        f.close()

    """
        Brief: Cet accesseur permet de retourner les coordonnées du coin haut droit
               du rectangle formé par la région créée. Le coin bas gauche étant toujours
               (0,0), il est sous-entendu.
        Return: Un tuple de deux entiers représentant les coordonnées du coin haut droit
               du rectangle formé par la région créée.
    """
    def get_general_boundaries(self):
        return self.boundaries

    """
        Brief: Cette fonction converti les données générées en un fichier CSV
               qui pourra être introduit dans la base de données.
    """
    def create_csv_file(self):
        f = open("../csv_files/VILLES.csv", 'w', encoding="utf-8")
        i = 0
        for c in self.cities:
            i += 1
            f.write('{0},"{1}",\n'.format(c[0], c[1]))
        f.close()

