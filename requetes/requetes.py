import pymysql

class Requetes:
    def __init__(self, user, password):
        self.con = pymysql.connect( host='localhost',
                            user=user,
                            password=password,
                            db='reseau_electrique')
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()


    def execute(self, cmd):
        self.cur.execute(cmd)
        return self.fetch_cursor()


    def fetch_cursor(self):
        result = []
        for tup in self.cur:
            line = []
            for attr in tup:
                line.append(attr)
            result.append(line)
        return result

