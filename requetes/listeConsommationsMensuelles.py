
class ListeConsommationsMensuelles:
    def __init__(self, req):
        self.execute = req.execute

    def get_data(self, aid):
        return self.execute("SELECT SUBSTR(CAST(Mois AS CHAR) FROM 1 FOR 7), Puissance FROM ConsommationsMensuelles WHERE Aid={}".format(aid))

