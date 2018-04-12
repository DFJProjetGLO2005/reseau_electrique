class ListeAbonnes:
    def __init__(self, req):
        self.execute = req.execute

    def get_data(self, aids):
        aids = "({})".format(", ".join(str(a) for a in aids))
        return self.execute("SELECT Aid, Nom, Telephone FROM Abonnes WHERE Aid in {};".format(aids))
