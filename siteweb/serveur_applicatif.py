from flask import Flask
from flask import render_template
app = Flask(__name__)

# Lorsque l'application roule, entre l'adresse donnée sur un browser.
# Les fichiers HTMLS vont dans ./templates
# Les autres fichiers vont dans ./static


@app.route("/")                             # vers l'élément racine "/"
def main():                                 # point d'entrée
    return render_template("index.html")        # rendu d'une page .html

@app.route("/ProchainePage")                # doit concorder avec l'attribut href de la balise qui déclenche la fonction
def ProchainePag():                         # le nom de fonction n'a pas d'importance
    var_python = "Python vous salue"
    return render_template("Page2.html", var_html = var_python)


if __name__ == "__main__":
    app.run()
