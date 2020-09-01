import psycopg2
from models import user
import config

def insertUser(name,lastname,email,password):
    conn=psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )
    cursor=conn.cursor()
    cursor.execute(f"INSERT INTO usuarios VALUES((SELECT MAX(id)+1 FROM usuarios),'{name}','{lastname}','{email}','{password}',CURRENT_TIMESTAMP)")
    conn.commit()
    cursor.close()
    conn.close()
    return True

def logIn(email,password):
    conn=psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )
    cursor=conn.cursor()
    cursor.execute(f"SELECT * FROM usuarios WHERE email = '{email}' AND contrasena ='{password}'")
    existe=cursor.fetchall()
    cursor.close()
    conn.close()
    if len(existe)>0:
        theUser=user.User(existe[0][0],existe[0][1],existe[0][2],existe[0][3],existe[0][4])
        return theUser
    else:
        return False
    
