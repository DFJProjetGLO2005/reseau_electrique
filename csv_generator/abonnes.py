import dill as pickle
import random

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


def gen_consommations_mensuelles(aid, graph):
    min_puissance = random.randint(1000,10000)
    variation = random.randint(100, 3000)
    max_puissance = min_puissance + variation
    for y in range(graph.time_limits[0], graph.time_limits[1]):
        for m in range(1,12):
            mois = "{0:4=0d}-{1:2=0d}-01 00:00:00".format(y, m)
            puissance = round(random.uniform(min_puissance, max_puissance) , 3)
            graph.tuples['CONSOMMATIONSMENSUELLES'].append([aid, mois, puissance])
