import os, sys, subprocess, platform, webbrowser

"""
    Brief: Cette fonction permet d'effacer le contenu de la console.
"""
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Scripts du dossier /csv_generator
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.system("python csv_generator/main.py")
os.chdir("sql_scripts")

# Scripts du dossier /sql_scripts
clear_screen()
print("------------------------------------------------------")
print("Création de la base de données sur votre serveur MySql\n")
utilisateur = input("Nom d'utilisateur: ")
os.system("mysql -u {0} -p < main.sql".format(utilisateur))   

# Scripts du dossier /siteweb
print("Vous serez maintenant appelé à entrer vos information de nouveau afin d'activer le serveur web.")
os.system("python ../siteweb/serveur_applicatif.py")
