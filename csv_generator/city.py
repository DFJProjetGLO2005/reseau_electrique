import random
import dill as pickle
import util

# Choisir une précision après la virgule fixe pour les coordonnées
# Pour chaque nouvelle ville, augmenter de la plus petite untié possible
# afin qu'un point ne puisse pas être à la limite de deux villes
# Conserver les frontières de la région entière

# Conserver les noms de villes dans un fichier pkl

class CityGenerator:
    def __init__(self):
        self.load_city_names()
        self.cities = []
        self.generate_cities()
        self.create_csv_file()
            


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


    def generate_one_city(self, lon, lat, width, height): 
        name = self.choose_name()
        self.cities.append([name,
                            'POLYGON(({} {}, {} {}, {} {}, {} {}, {} {}))'.format(
                            lon, lat,
                            lon + width, lat,
                            lon + width, lat + height,
                            lon, lat + height,
                            lon, lat)])


    def choose_name(self):
        name = random.choice(self.names)
        self.names.remove(name)
        return name


    def load_city_names(self):
        f = open("data/cities.pkl", 'rb')
        self.names = pickle.load(f)
        f.close()

    def get_general_boundaries(self):
        return self.boundaries

    def create_csv_file(self):
        f = open("../csv_files/VILLES.csv", 'w', encoding="utf-8")
        i = 0
        for c in self.cities:
            i += 1
            f.write('{0},"{1}",\n'.format(c[0], c[1]))
        f.close()

if __name__ == "__main__":
    city_generation = CityGenerator()
