class ListeAbonnes:
    def __init__(self, req):
        self.execute = req.execute

    def get_data(self, aids):
        data = []
        for a in aids:
            data.append(self.execute("SELECT Aid, Nom, Telephone FROM Abonnes;"))
        return data
