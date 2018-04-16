from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import flash
import util
import sys, os, getpass
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../requetes")
from listeConsommationsMensuelles import ListeConsommationsMensuelles
from listeEquipements import ListeEquipements
from listeCentrales import ListeCentrales
from listeAbonnes import ListeAbonnes
from listeVilles import ListeVilles
from listeBris import ListeBris

app = Flask(__name__)
req = util.connect_db()
util.define_admin_password(req)



"""
    Brief: Ce conteneur permet d'échanger des données entre
           les différentes pages et évite de dupliquer inutilement
           les requêtes à la base de données.
"""
cache = {}



"""
    Brief: Cette fonction permet de rendre la racine du siteweb.
           Chacun de ses bouton déclenche une autre fonction associée.
           Le radio button règle l'ordre de présentation des bris.
           Cette fonction inscrit des données dans le conteneur global cache.
           La page affichée contient trois boutons:
           liste_villes: Qui charge la page listeVilles.html
           liste_centrales: Qui charge la page listeCentrales.html
           liste_bris: Qui vérifie l'état du sélecteur radio "ordre_bris"
                       et qui charge la page listeBris.html
"""
@app.route("/", methods=["GET", "POST"])              
def main():
    global cache
    if request.method == 'POST':
        if request.form.get("button") == "liste_villes":
            return redirect(url_for('liste_villes'))
        elif request.form.get("button") == "liste_centrales":
            return redirect(url_for('liste_centrales'))
        else:
            cache["ordre_bris"] = request.form.get("ordre_bris")
            return redirect(url_for('liste_bris'))
    return render_template("index.html")





"""
    Brief: Cette fonction permet de rendre la page de la liste des bris.
           Elle puise et inscrit des données dans le conteneur global cache.
           Elle est préalable au chargement de la page des détails de bris.
           Cette page contient une série de boutons "bris_choisis" qui ont
           tous comme valeur l'identificateur du bris choisi.
           Ce bouton charge la page detailsBris.html
"""
@app.route("/listeBris", methods=["GET", "POST"])      
def liste_bris():
    global cache
    cache['liste_bris'] = ListeBris(req).get_data(cache["ordre_bris"])
    if request.method == 'POST':
        bris_choisi = request.form.get("bris_choisi")
        for bris in cache["liste_bris"]:
            if bris['eid'] == bris_choisi[0:9] and bris['date'] == bris_choisi[10:]:
                cache["details_bris"] = ListeBris(req).get_liste_details(bris)
                return redirect(url_for('details_bris'))
    return render_template("listeBris.html", IN=cache["liste_bris"])



"""
    Brief: Cette fonction permet de rendre la page des détails de bris.
           Elle puise et inscrit des données dans le conteneur global cache.
           Cette fonction ou liste_ville sont préalables à liste_abonnes. 
           Cette page contient deux boutons:
           "liste_abonnes": Qui affiche la liste des abonnées affectés
            par le bris courant via listeAbonnes.html
           "resoudre": Qui marque le bris sélectionné comme résolu
            en date de maintenant. Puisque l'utilisation abusive
            de ce bouton serait néfaste pour la base de données,
            il sera nécessaire de vérifier que le mot de passe entré
            dans la boîte "password" est correct.
"""
@app.route("/detailsBris", methods=["GET", "POST"])
def details_bris():
    global cache
    if request.method == 'POST':
        if request.form.get("button") == "liste_abonnes":
            cache["liste_abonnes"] = cache["details_bris"]["aids"]
            return redirect(url_for('liste_abonnes'))
        elif request.form.get("button") == "resoudre":
            if ListeBris(req).check_password(request.form.get("password")):
                ListeBris(req).resoudre_bris(cache["details_bris"]["eid"], cache["details_bris"]["date"])
                return redirect(url_for('liste_bris'))
            else:
                return redirect(url_for('attention'))
    return render_template("detailsBris.html", IN=cache["details_bris"]) 



"""
    Brief: Cette page affiche un avertissement comme quoi
           un mot de passe entré est incorrect.
"""
@app.route("/attention")
def attention():
    return render_template("attention.html")


"""
    Brief: Cette fonction permet de rendre la page de liste d'abonnées.
           La nature de la liste dépendra de si cette page a été chargée
           à partir de details_bris ou liste_ville. Elle puise donc des
           données du cconteneur cache. Cette fonction est préalable à
           la fonction liste_consommations_mensuelles et inscrit au 
           conteneur cache les informations qui y seront nécessaires.
           Cette page contient une série de boutons identifiés par "abonne_choisi".
           Chacun de ces boutons a comme valeur l'identificateur de l'abonné.
           Ce bouton charge la page listeConsommationsMensuelles.html
        
"""
@app.route("/listeAbonnes", methods=["GET", "POST"])
def liste_abonnes():
    global cache
    if request.method == 'POST':
        cache["liste_consommations_mensuelles"] = request.form.get("abonne_choisi") 
        return redirect(url_for('liste_consommations_mensuelles'))
    return render_template("listeAbonnes.html", IN=ListeAbonnes(req).get_data(cache["liste_abonnes"]))


"""
    Brief: Cette fonction permet de rendre la page d'historique de
           consommations. Elle consulte le contenur cache afin de
           connaître l'abonné visé. La fonction liste_abonnes
           est préalable à l'appel de cette fonction.
"""
@app.route("/listeConsommationsMensuelles", methods=["GET", "POST"])
def liste_consommations_mensuelles():
    global cache
    consommations = ListeConsommationsMensuelles(req).get_data(cache["liste_consommations_mensuelles"])
    return render_template("listeConsommationsMensuelles.html", IN=consommations, abonne=cache["liste_consommations_mensuelles"])






"""
    Brief: Cette fonction permet de rendre la page de la liste des
           centrales. Elle n'a pas besoin du conteneur cache.
"""
@app.route("/listeCentrales")
def liste_centrales():
    return render_template("listeCentrales.html", IN=ListeCentrales(req).get_data())



"""
    Brief: Cette fonction permet de rendre la page de la liste des
           villes. Elle est préalable à liste_equipements et 
           liste_abonnes. Elle puise et inscrit des informations
           au conteneur cache.
           Cette page contient une série de boutons ayant pour valeurs possibles:
           "abo*": Affiche la liste des abonnés qui habitent
            la ville * sélectionnée via listeAbonnes.html
           "equ*": Affiche la liste des équipements situés dans
            la vilel * sélectionnée via listeEquipements.html
            
"""
@app.route("/listeVilles", methods=["GET", "POST"])
def liste_villes():
    global cache
    if request.method == 'POST':
        if request.form.get("button")[0:3] == "abo":
            for v in cache["liste_villes"]:
                if v[0] == request.form.get("button")[4:]:
                    cache["liste_abonnes"] = v[1][1] 
            return redirect(url_for('liste_abonnes'))
        else:
            cache["liste_equipements"] = ListeEquipements(req).get_data(request.form.get("button")[4:])
            return redirect(url_for('liste_equipements'))
    cache["liste_villes"] = ListeVilles(req).get_data()
    return render_template("listeVilles.html", IN=cache["liste_villes"])


"""
    Brief: Cette fonction permet de rendre la page de la liste
           des équipements. Elle puise ses données dans le conteneur cache.
"""
@app.route("/listeEqupements")
def liste_equipements():
    global cache
    return render_template("listeEquipements.html", IN=cache["liste_equipements"])

if __name__ == "__main__":
    app.run()
