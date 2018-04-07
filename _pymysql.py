from requetes import Requetes





if __name__ == "__main__":
    req = Requetes('root', 'tetuda')
    bris = req.get_bris()
    req.trouver_meteo(bris[0]["ville"], bris[0]["date"])
