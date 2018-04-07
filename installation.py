import os, subprocess, platform

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



while True:
    clear_screen()
    print("------------------------------------------------------")
    print("Création de la base de données sur votre serveur MySql\n")
    message = subprocess.getoutput(["mysql", "-u", input("Nom d'utilisateur: "), "-p", "<",  "main.sql"])
    if message:
        print(message)
    else:
        break

print("\nL'installation a réussi. Vous pouvez désormais tester l'application à l'adresse ci-bas.\n")
subprocess.call(["python", "../siteweb/serveur_applicatif.py"])


