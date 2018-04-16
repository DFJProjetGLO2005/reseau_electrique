import sys, os, getpass
from pathlib import Path
from hashlib import sha256



"""
    Brief: Cette fonction permet à l'hôte du serveur
           applicatif de se connecter à la base de 
           données afin de pouvoir lui envoyer des requêtes
    Param[in]: La classe Requetes
    Return: Une instance de la classe Requetes qui permet
            d'envoyer des requêtes à la base de données
            à laquelle elle est connectée.
"""
def connect_db(Requetes):
    while True:
        try:
            print("------------------------------------------------")
            print("Activation du serveur web")
            return Requetes(input("  Nom d'utilisateur mysql: "),
                            getpass.getpass("  Mot de passe: "))
        except Exception as e: print("\n  Nom d'utilisateur ou mot de passe incorrect.\n")


"""
    Brief: Cette fonction crée un mot de passe d'administration dans la base de données
           Il est pas défaut "12345"
    Param[in]: Une instance de la classe Requetes permettant d'acheminer les requêtes
               nécessaires vers la base de données.
"""
def define_admin_password(req):
    req.execute('INSERT INTO AdminPassword VALUES ("{}");'.format(hash_password("12345")))
    req.con.commit()

"""
    Brief: Cette fonction change le dossier courant d'exécution pour celui du script
"""
def cd_script_path():
    os.chdir(str(Path(__file__).resolve().parent)) 

"""
    Brief: Cette fonction prend une entrée texte, la hache et retourne son résultat haché
    Param[in]: Le texte a hacher
    Return: Le texte haché
"""
def hash_password(text):
    return sha256(text.encode()).hexdigest()

