import os
import sqlite3 as sq

BASE_DIR =  os.path.dirname(os.path.abspath(__file__))
ROOT_DIR =  os.path.dirname(BASE_DIR)

DB_PATH = os.path.join(ROOT_DIR, "database.db")

conn = sq.connect(DB_PATH)

cursor = conn.cursor()


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


nova_sessao = ("011","Janeiro", "01/01/2026", "minoxidil", "frontal","imagempath","estavel","taltal")

cursor.execute('INSERT INTO sessoes VALUES (?,?,?,?,?,?,?,?)',nova_sessao)

conn.commit()

cursor.execute('SELECT * FROM sessoes')
print(cursor.fetchall())

conn.close()