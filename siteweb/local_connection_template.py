import pymysql

def connect():
    return pymysql.connect( host='localhost',
                            user='UTILISATEUR',
                            password='MOTDEPASSE',
                            db='NOMBASEDONNEES')
