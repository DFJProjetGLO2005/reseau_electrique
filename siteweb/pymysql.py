import pymysql
import pymysql.cursors
from local_connection import connect



def requete(cur, req):
    try:
        cur.execute(req)                                    #exécuter une requête
        display_cursor(cur)
    except Exception as e:
        print(e)

def display_cursor(cur):
    for tup in cur:
        for attr in tup:
            print('\t' + str(attr), end="")
        print()


if __name__ == "__main__":
    conn = connect()
    cur=conn.cursor()                                   #le curseur
    while True:
        requete(cur, input("req > "))                   
    
       
    cur.close()
    conn.close()                   

