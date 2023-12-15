from main import DB_FILE, TABLE_NAME

import sqlite3


connection_ = sqlite3.connect(DB_FILE)
cursor = connection_.cursor()

# Usar o select
# Seleciona todas as colunas onde o id é 3
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = "3"'
)

# Pegar uma linha
# Depois de usar o cursor ele esgota
row_ = cursor.fetchone()
_id, name, weight = row_
print(_id, name, weight)

print()
print("==="*10)
print()

# Usar o select
cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    )

# Percorrer por todos os valores obtidos do select
# Pegar todas as linhas
for row in cursor.fetchall():
    _id, name, weight = row
    print(_id, name, weight)

cursor.close()
connection_.close()