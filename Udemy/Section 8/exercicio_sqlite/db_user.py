from pathlib import Path
import sqlite3

class Database:
    DB_FILE = Path(__file__).parent / 'db.sqlite3'
    connection = None


    def __init__(self, db_file=DB_FILE):
        self._db_file = db_file
        self.connection = None
        self.cursor = None


    def connect_(self):
        self.connection = sqlite3.connect(self._db_file)
        self.cursor = self.connection.cursor()


    def exit_(self):
        self.cursor.close()
        self.connection.close()


    def save_(self):
        self.connection.commit()

    # Função funcionando
    def create_table(self, table_name, *columns):
        # Contruir a tabela
        table = f'CREATE TABLE IF NOT EXISTS {table_name}'
        table = f'{table}(id INTEGER PRIMARY KEY AUTOINCREMENT, '

        table = table + ' , '.join(columns) + ')'

        # Criar tabela
        self.cursor.execute(table)   

    # Função funcionando
    def insert_user(self, table_name, *args):    
        insert_ = f'INSERT INTO {table_name} (name, age) VALUES(?, ?)'

        self.cursor.execute(insert_, args)
        self.save_()

    # Função funcionando
    def delete_user(self, table_name, id):
        delete = f'DELETE FROM {table_name} WHERE id = {id}' 
        self.cursor.execute(delete)
        self.save_()

    # Função funcionando
    def update_user(self, table_name, name, age, id):
        update = f'UPDATE {table_name} SET name="{name}", age={age} WHERE id = {id}'
        self.cursor.execute(update)
        self.save_()

    # Função Funcionando
    def select_user(self, table_name):
        select = self.cursor.execute(f'SELECT * FROM {table_name} ')

        for row in select.fetchall():
            _id, name, weight = row
            print(_id, name, weight)
        

    def __del__(self):
        try:
            self.cursor.close()
            self.connection.close()
            print('Conexão encerrada a força')
        except sqlite3.ProgrammingError:
            print('Conexão já encerrada')



if __name__ == '__main__':
    connect_db = Database()
    connect_db.connect_()

    connect_db.exit_()
    


    