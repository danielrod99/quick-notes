import psycopg2
import config
def createNote(idUser,title,descripcion):
    conn=psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )
    cursor=conn.cursor()
    cursor.execute(f"INSERT INTO notas VALUES((SELECT MAX(id)+1 FROM notas),{idUser},'{title}','{descripcion}',CURRENT_TIMESTAMP)")
    conn.commit()
    cursor.close()
    conn.close()

def allNotes(idUser):
    conn=psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )
    cursor=conn.cursor()
    cursor.execute(f"SELECT * FROM notas WHERE id_usuario = {idUser}")
    notas=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return notas
def deleteNote(idUser,title):
    conn=psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password
    )
    cursor=conn.cursor()
    cursor.execute(f"DELETE FROM notas WHERE id_usuario = {idUser} AND titulo = '{title}'")
    conn.commit()
    cursor.close()
    conn.close()