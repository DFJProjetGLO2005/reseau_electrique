import sys, os, getpass
from hashlib import sha256
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("../requetes")
import requetes

"""
    Brief: Cette fonction permet à l'hôte du serveur
           applicatif de se connecter à la base de 
           données afin de pouvoir lui envoyer des requêtes
    Return: Une instance de la classe Requetes qui permet
            d'envoyer des requêtes à la base de données
            à laquelle elle est connectée.
"""
def connect_db():
    while True:
        try:
            print("------------------------------------------------")
            print("Activation du serveur web")
            return requetes.Requetes(input("  Nom d'utilisateur mysql: "),
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




def hash_password(text):
    return sha256(text.encode()).hexdigest()

