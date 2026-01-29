import os
import sqlite3 as sq

BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
ROOT_DIR =  os.path.dirname(BASE_DIR)

DB_PATH = os.path.join(ROOT_DIR, "database.db")

conn = sq.connect(DB_PATH)

cursor = conn.cursor()


cursor.execute('DROP TABLE IF EXISTS sessoes')

conn.commit()
 
## SE TABELA NÃO EXISTIR
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessoes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               data TEXT,
               tratamento TEXT,
               photo_frontal TEXT,
               photo_entradas TEXT,
               photo_midscalp TEXT,
               photo_coroa TEXT,
               frontal_area TEXT,
               entradas_area TEXT,
               midscalp_area TEXT,
               coroa_area TEXT,
               obs TEXT
               )

''')



conn.commit()
conn.close()


def registrar_sessao(data,tratamento,photo_frontal,photo_entradas,photo_midscalp, photo_coroa, frontal_estado, entradas_estado, midscalp_estado,coroa_estado,obs):

    conn = sq.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(" INSERT INTO sessoes (data, tratamento, photo_frontal, photo_entradas, photo_midscalp, photo_coroa,frontal_area,entradas_area,midscalp_area,coroa_area,obs) VALUES (?,?,?,?,?,?,?,?,?,?,?)", (data,tratamento,photo_frontal,photo_entradas,photo_midscalp,photo_coroa,frontal_estado,entradas_estado, midscalp_estado, coroa_estado,obs))

    conn.commit()
    conn.close()