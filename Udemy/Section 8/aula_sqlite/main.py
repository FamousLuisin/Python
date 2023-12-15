from pathlib import Path

import sqlite3

# Diretorio do arquivo
# Sem o .parente é o caminho do arquivo
ROOT_DIR = Path(__file__).parent

# Caminho do Data base
DB_FILE = ROOT_DIR / 'db.sqlite3'

# Nome da tabela
TABLE_NAME = 'customers'

# CRUD =  CREATE READ UPDATE DELETE
# SQL = INSERT SELECT UPDATE DELETE

# Conectar ao banco de dados SQLite
connection_ = sqlite3.connect(DB_FILE)

# Cursor serve para o programa interagir com os resultados de uma consulta SQL
# Interaje linha por linha
# Ponte entre a aplicação e os resultados obtidos de uma consulta a um db
cursor = connection_.cursor()

# WARNING: CUIDADO (vai apagar todos os valores da tabela)
# Apaga tudo daquela tabela
cursor.execute(
    f'DELETE FROM {TABLE_NAME} '
)

# Zerar a sequencia de ids
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection_.commit()

# Criar uma tabela
cursor.execute(
   f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
   '('
   'id INTEGER PRIMARY KEY AUTOINCREMENT,'
   'name TEXT,'
   'weight REAL'
   ')'
)
connection_.commit()

# Registrar valores
# Como o id é AUTOINCREMENT não precisa ser colocado
# CUIDADE: sql injection
# Evitar: Usar binding / placeholders > (?, ?), [valor1, valor2]
sql_inserir = (
    f'INSERT INTO {TABLE_NAME}' 
    '(name, weight) '
    'VALUES' 
    '(:nome, :peso)')

# Adicionar um unico valor
# cursor.execute(sql_inserir, ['Mike', 55])

# Adicionar mais de um valor, tem q usar um iteravel de iteraveis
# cursor.executemany(sql_inserir, [['Mike', 70], ['Jhonson', 50], ['Mari', 45.7], ['Luh', 52]])

# Adicionar um dicionario
# Nesse caso os parametros do placeholde / bindign devem ser :nome_chave_dicionario
# cursor.execute(sql_inserir, {'nome': 'Luís', 'peso': 50.5})

# Adicionar mais de um dicionario
cursor.executemany(sql_inserir, (
    {'nome': 'Luís', 'peso': 50.5},
    {'nome': 'Giih', 'peso': 70.5},
    {'nome': 'Mike', 'peso': 69.5}
    ))



connection_.commit()




if __name__ == '__main__':

    # Deletar
    # Precisamos de um where para deletar a linha q queremos
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "2"'
    )

    # Update
    # Precisamos do set para escolhermos oq iremos mudar
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="None", weight=0 '
        'WHERE id = 1'
    )
    
    cursor.execute(
    f'SELECT * FROM {TABLE_NAME} '
    )

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    

    connection_.commit()

    cursor.close()
    connection_.close()