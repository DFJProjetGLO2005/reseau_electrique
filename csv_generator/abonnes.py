import dill as pickle
import random

"""
    Brief: Cette fonction génère un abonné aléatoirement au réseau électrique.
    Arg[p_id]: L'identificateur du point de raccordement associé à l'utilisateur.
    Arg[graph]: Une instance de Graph pour laquelle on désire associer l'abonné.
    Return: L'identificateur de l'abonné sous forme de Int.
"""
def gen_abonnnes(p_id, graph):
    aid = len(graph.tuples["ABONNES"])
    f = open("data/names.pkl", "rb")
    nom = random.choice(pickle.load(f))
    f.close()
    tel = "{0}-{1:0=4d}".format(
            random.choice(["832", "657", "208", "834", "123", "456"]),
            random.randint(0,9999))
    graph.tuples["ABONNES"].append([aid, nom, tel, p_id])
    gen_consommations_mensuelles(aid, graph)
    return aid

"""
    Brief: Cette fonction génère des consommations mensuelles aléatoires par mois pour
           un abonné pour toute la plage temporelle d'une instance de Graphe.
           Par souci de réalisme, chaque abonné aura une consommation plus ou moins
           changeante de mois en mois.
    Arg[aid]: L'identificateur de l'abonné
    Arg[graph]: L'instance de Graph pour laquelle on veut créer ces consommations.
"""
def gen_consommations_mensuelles(aid, graph):
    min_puissance = random.randint(1000,10000)
    variation = random.randint(100, 3000)
    max_puissance = min_puissance + variation
    for y in range(graph.time_limits[0], graph.time_limits[1]):
        for m in range(1,13):
            mois = "{0:4=0d}-{1:2=0d}-01 00:00:00".format(y, m)
            puissance = round(random.uniform(min_puissance, max_puissance) , 3)
            graph.tuples['CONSOMMATIONSMENSUELLES'].append([aid, mois, puissance])
