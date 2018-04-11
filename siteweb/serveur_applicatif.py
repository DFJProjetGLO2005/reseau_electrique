from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

# Lorsque l'application roule, entre l'adresse donnée sur un browser.
# Les fichiers HTMLS vont dans ./templates
# Les autres fichiers vont dans ./static


@app.route("/")                             # vers l'élément racine "/"
def main():                                 # point d'entrée
    print(request.args.get('idText'))
    maliste = {'hello' : 10}
    return render_template("index.html", maliste = maliste)        # rendu d'une page .html

@app.route("/ProchainePage")                # doit concorder avec l'attribut href de la balise qui déclenche la fonction
def ProchainePag():                         # le nom de fonction n'a pas d'importance
    return render_template("Page2.html")


if __name__ == "__main__":
    app.run()
