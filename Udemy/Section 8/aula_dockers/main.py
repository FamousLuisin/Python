#importar pymysql
import pymysql
# Poder alterar os cursores usados
import pymysql.cursors
# Fazer um load do .env para o codigo python como variaveis de ambiente
import dotenv
# Pegar os valores do .env nas variaveis de ambiente os.environ['']
import os

TABLE_NAME = 'customers'

dotenv.load_dotenv()

# Fazer a conexão
# host(Local da aplicação) / user(usuario) / password(senha) / database(base de dados)
connection = pymysql.connect(
    host = os.environ['MYSQL_HOST'],
    user = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE'],
    cursorclass=pymysql.cursors.DictCursor,
)

# Context maneger da conexão
with connection:
    # Context maneger do cursor
    with connection.cursor() as cursor:
        # Não é mais necessario fechar as conexões
        # Codigo

        # Criar tabela
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(50) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY(id)'
            ') '
        )

        # WARNING: Limpa a tabela
        cursor.execute(
            f'TRUNCATE TABLE {TABLE_NAME}'
        )

    
    # Salvar uma alteração
    connection.commit()

    # Inserir um valor com placeholder
    with connection.cursor() as cursor:
        # Não é mais necessario fechar as conexões
        # Codigo

        # Fazer consulta
        # Mandar a consulta e os valore separados
        # Dessa forma o sistema não irá entender os comandos como comandos e sim como valores
        # Placeholders usa o %s
        # Serve para evitar sql injection
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%s, %s) '
        )

        # Dados "normais"
        data = ('Luisin', 25)

        # Consultar
        cursor.execute(sql, data)

    connection.commit()

    # Inserir um valor de dicionario com placeholder
    with connection.cursor() as cursor:
        # Deve colocar o nome da chave que qr q o valor seja usado
        # No lugar em q qr q esse valor seja salvo
        # Igual logo a baixo
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%(nome)s, %(idade)s) '
        )

        # Dados vindo de dicionarios
        data = {
            "nome": "Noki",
            "idade": 22,        
        }

        # Consultar
        cursor.execute(sql, data)

    connection.commit()

    # Inserir varios dicionaris usando tbm placeholder
    with connection.cursor() as cursor:   
        
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%(nome)s, %(idade)s) '
        )

        # Dados vindo de um iteravel de dicionarios
        data_iteravel = (
            {"nome": "Mike","idade": 22}, 
            {"nome": "Lulu", "idade": 21},
            {"nome": "Ana", "idade": 20}
        )

        # Deve ser iteraveis o dados entregues
        # Iteraveis dentro de iteraveis exemplo: tuplas dentro de tuplas
        # ou dicionarios dentro de iteraveis exemplo: lista de dicionarios
        cursor.executemany(sql, data_iteravel)

    connection.commit()

    # Inserir varias duplas usando tbm um placeholder
    with connection.cursor() as cursor:
        
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%s, %s) '
        )

        # Dados vindo de um iteravel de tuplas
        data_iteravel = (
            ("Giih", 23),
            ("Patu", 26)
        )

        # Deve ser iteraveis o dados entregues
        # Iteraveis dentro de iteraveis exemplo: tuplas dentro de tuplas
        # ou dicionarios dentro de iteraveis exemplo: lista de dicionarios
        cursor.executemany(sql, data_iteravel)

    connection.commit()

    # Ler valores usando SELECT (Não é necessario commit)
    with connection.cursor() as cursor:
        
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )

        cursor.execute(sql)

        # O cursor fica com um iteravel que pode ser usado, mas é esgotado
        for row in cursor.fetchall():
            print(row)

    # Ler valores usando SELECT WHERE (Não é necessario commit)
    with connection.cursor() as cursor:
        print("====="*4)
        id_menor = 2
        id_maior = 4
        # Sempre usar placeholders
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )

        cursor.execute(sql, (id_menor, id_maior))

        # O cursor fica com um iteravel que pode ser usado, mas é esgotado
        # Ver qual consulta vái ser ultilizada
        # print(cursor.mogrify(sql, (id_menor, id_maior)))
        for row in cursor.fetchall():
            print(row)

    # Apagar valores DELETE WHERE (Precisa de commit)
    with connection.cursor() as cursor:
        print("====="*4)
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )

        cursor.execute(sql, 2)
        # Caso nn faça o commit a base de dados nn gera alterada
        # a alteração será gerada apenas em campo virtual
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row in cursor.fetchall():
            print(row)

    
    # Alterar valores UPDATE WHERE (Precisa de commit)
    with connection.cursor() as cursor:
        print("====="*4)
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET name = %s, age = %s '
            'WHERE id = %s'
        )

        cursor.execute(sql, ('Julia', 27, 5))
        # Caso nn faça o commit a base de dados nn gera alterada
        # a alteração será gerada apenas em campo virtual

        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data = cursor.fetchall()

        print('For 1:')
        # O unbaffet serve para alguns casos como internet lenta ou uma grande quantidade de dados
        # ele salva na memoria do cursor apenas a linha atual
        # se for o caso usar o comando .fetchall_unbuffered
        for row in data:
            # Dictcursor
            # _id, name, age = row.items()
            print(row)

        # Fazer um scroll do cursor para cima
        # print('For 2:')
        # # cursor.scroll(0, 'absolute')
        # for row in cursor.fetchall():
        #     print(row)
            
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) VALUES (%s, %s) '
        )

        # Dados "normais"
        data = ('Jojo', 17)

        # Consultar
        cursor.execute(sql, data)

        cursor.execute(f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1')
        lastIdFromSelect = cursor.fetchone()


        # Numero de linhas alteradas
        print()    
        print('resultFromSelect:', resultFromSelect)
        print('resultFromSelect:', len(data))
        # Pega o numero de linhas alteradas na ultima operação
        print('rowcount:', cursor.rowcount)
        # Ultimo id inserido
        print('lastrowid:', cursor.lastrowid) # Precisa ter sido inserido "recentemente" (Ultima operação)
        print('lastrowid na mão:', lastIdFromSelect)
        # Em que linha esta o cursro
        print('rownumber: ', cursor.rownumber)
    
    connection.commit()


        