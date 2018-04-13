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


def define_admin_password(req):
    req.execute('DROP TABLE IF EXISTS AdminPassword;')
    req.execute('CREATE TABLE AdminPassword (Password CHAR(64));')
    req.execute('INSERT INTO AdminPassword VALUES ("{}");'.format(hash_password("12345")))
    req.con.commit()




def hash_password(text):
    return sha256(text.encode()).hexdigest()

