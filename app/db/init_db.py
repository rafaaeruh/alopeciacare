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



cursor.execute('SELECT * FROM sessoes')
print(cursor.fetchall())

conn.close()