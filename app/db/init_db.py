import os
import sqlite3 as sq

BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
ROOT_DIR =  os.path.dirname(BASE_DIR)

DB_PATH = os.path.join(ROOT_DIR, "database.db")






conn = sq.connect(DB_PATH)

cursor = conn.cursor()

## SE TABELA NÃO EXISTIR
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessoes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               mes TEXT,
               data TEXT,
               tratamento TEXT,
               area TEXT,
               photo_path TEXT,
               status TEXT,
               obs TEXT
               )

''')

conn.commit()



def registrar_sessao(id,mes,data,tratamento,area,imagem_path,status,obs):
    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO sessoes VALUES (?,?,?,?,?,?,?,?)", (id,mes,data,tratamento,area,imagem_path,status,obs))

    conn.commit()
    conn.close()


registrar_sessao(27,"Agosto","19/08/2026","Biotina","Linha frontal","/home/Images","estável","nada a declarar")

cursor.execute('SELECT * FROM sessoes')
print(cursor.fetchall())

conn.close()