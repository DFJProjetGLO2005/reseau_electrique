import dill as pickle
import random
import util

def gen_meteo(graph):
    end = graph.time_limits[1]
    i = 0
    for ville in get_cities():
        i += 1
        util.display_loading("Création des données météo", i/80)
        annee = graph.time_limits[0]
        while annee < end:
            for mois in range(1, 12):
                for jour in range(1, 28):
                    for heure in range(0, 23):
                        temps = "{0:4=0d}-{1:2=0d}-{2:2=0d} {3:2=0d}:00:00".format(annee, mois, jour, heure)
                        temperature = random.randint(-20,30)
                        humidite = round(random.uniform(50, 100), 3)
                        pression = round(random.uniform(-2, 2), 3)
                        pluie = random.randint(0, 4)
                        neige = random.randint(0, 4)
                        couv_neige = random.randint(0, 4)
                        graph.tuples["CONDITIONSMETEOROLOGIQUES"].append([ville, temps, temperature, humidite, pression, pluie, neige, couv_neige])
            annee += 1



def get_cities():
    with open("data/cities.pkl", "rb") as f:
        return pickle.load(f) 

