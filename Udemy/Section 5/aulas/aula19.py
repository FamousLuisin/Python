# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

from abc import ABC, abstractmethod

class Notification(ABC):
    def __init__(self, msg) -> None:
        self.mensagem = msg

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificationEmail(Notification):
    def enviar(self):
        print('Email enviando:', self.mensagem)
        return True

class NotificationSms(Notification):
    def enviar(self):
        print('SMS enviado:', self.mensagem)
        return False

# notification: str (Está dizendo que o atributo recebido deve ser do tipo str)
def notificar(notification: Notification):
    noticacao_enviada = notification.enviar()
    
    if noticacao_enviada:
        print('Enviada')
    else:
        print('Não enviada')

notificar(NotificationEmail('Teste Email'))
notificar(NotificationSms('Teste SMS'))