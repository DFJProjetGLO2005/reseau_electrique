import sys, os, getpass
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
