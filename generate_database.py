import os, subprocess, platform

### Recevoir le feedback de mysql et redemander les informations en cas d'échec
### Annoncer le nécessaire pour que l'installateur fonctionne
###     -mysql au path
###     -python au path
###     -autres?


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")



abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
subprocess.call(["python", "csv_generator/main.py"])
os.chdir("sql_scripts")
sql_script = "main.sql"
while True:
    clear_screen()
    nom_bd = input("Veuillez créer une base de données vierge sur votre serveur mysql local et entrez son nom ici: ")
    user = input("Veuillez entrer votre nom d'utilisateur: ")
    print("\nEn entrant votre mot de passe, mysql introduira les données générées dans la base de données {}.".format(nom_bd))
    message = subprocess.getoutput(["mysql", "-u", user, "-p", nom_bd, "<",  sql_script])
    if message:
        print(message)
        aide = input("\nIl se peut qu'un des champs ait mal été rempli. Si vous éprouvez des problèmes à répétition, veuillez entrer H pour obtenir de l'aide. Sinon, appuyez sur enter pour recommencer.")
        if aide.upper() == "H":
            clear_screen()
            input("aide")
    else:
        input("\nL'installation a réussi.")
        break




