from requetes import Requetes
from listeCentrales import ListeCentrales
from listeVilles import ListeVilles





if __name__ == "__main__":
    req = Requetes('root', 'tetuda')
    cent = ListeVilles('root', 'tetuda')
    for v, c in cent.requete().items():
        print(v, c)
    #bris = req.get_liste_bris("estimation_conso")# nb_abonnes / date / estimation_conso 
    #for b in bris:
    #    print(b)
