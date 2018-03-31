import random

def gen_bris(graph):
    bris_qty = random.randint(10, 100)
    for i in range(bris_qty):
        eid = random.choice(graph.tuples["EQUIPEMENTS"])[0]
        d_annee = random.randint(graph.time_limits[0], graph.time_limits[1] - 1) 
        d_mois = random.randint(1, 12)
        d_jour = random.randint(1, 28)
        d_heure = random.randint(0, 23)
        d_minute = random.randint(0, 59)
        d_seconde = random.randint(0, 59)
        debut = "{0:4=0d}-{1:2=0d}-{2:2=0d} {3:2=0d}:{4:2=0d}:{5:2=0d}".format(d_annee, d_mois, d_jour, d_heure, d_minute, d_seconde)
        if random.choice([0,0,0,1]):
            f_annee = random.randint(d_annee, graph.time_limits[1] - 1) 
            f_min_mois = d_mois if f_annee == d_annee else 1
            f_mois = random.randint(f_min_mois, 12)
            f_min_jour = d_jour if f_annee == d_annee and f_mois == d_mois else 1
            f_jour = random.randint(f_min_jour, 28)
            f_min_heure = d_heure if f_annee == d_annee and f_mois == d_mois and f_jour == d_jour else 0
            f_heure = random.randint(f_min_heure, 23)
            f_min_minute = d_minute if f_annee == d_annee and f_mois == d_mois and f_jour == d_jour and f_heure == d_heure else 0
            f_minute = random.randint(f_min_minute, 59)
            f_min_seconde = d_minute if f_annee == d_annee and f_mois == d_mois and f_jour == d_jour and f_heure == d_heure and f_minute == d_minute else 0
            f_seconde = random.randint(f_min_seconde, 59)
            fin = "{0:4=0d}-{1:2=0d}-{2:2=0d} {3:2=0d}:{4:2=0d}:{5:2=0d}".format(f_annee, f_mois, f_jour, f_heure, f_minute, f_seconde)
        else:
            fin = "NULL"
        graph.tuples["BRIS"].append([eid, debut, fin])

