# Metodo normal (instancia) recebe self
# Metodo de class recebe o cls
class Connection:
    
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    # Metodo para setar user (setter são metodos de instancias)
    def set_user(self, user):
        # setter
        self.user = user

    # Metodo para setar password
    def set_password(self, password):
        # setter
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


# c1 = Connection()
c1 = Connection.create_with_auth('Noki', '123')
# c1.set_user('Noki')
# c1.set_password('123')
print(c1.user)
print(c1.password)