# Abstração
from pathlib import Path

# __file__ = caminho do modulo
# Pegar o caminho do log.txt
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    # Abstração (Voce esta usando a superclasse, mas qr que usem as subclasses)
    # Assinatura do Método (é tudo qu pertence ao metodo)
    def _log(self, msg):
        raise NotImplementedError('Implementar o metodo Log')
    
    # O metodo log_erro não precisa ser redefinido
    def log_error(self, msg):
        # Error: {msg} > É a msg que esta sendo mandada para o metodo _log
        # Ta passando a mensagem em formato de f-string
        return self._log(f'Error: {msg}')
    
    # O metodo log_success não precisa ser redefinido
    def log_success(self, msg):
        # Success: {msg} > É a msg que esta sendo mandada para o metodo _log
        return self._log(f'Success: {msg}')

# Mixin (adcionar funcionalidades em sua herança multipla)
# Adicionar coisas dentro das outras classes
# Função para salvbar em um txt
class LogFileMixin(Log):
    # Sobrepor um metodo a assinatura dele deve ser identica
    # Não pode haver mudança nem de tipo nem de retorno
    def _log(self, msg):
        # Cria msg formatada
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        # adicionar logs
        # Não usar 'w', pois ele sobreescreve o arquivo
        # Usar 'a', pois ele apenas adiciona ao arquivo
        print("Salvando no log...")
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

# Função para imprimir na tela
class LogPrintMixin(Log):
    # Método de uso interno da classe (possui um _)
    # O metodo _log ta recebendo a msg do metodo log_erro 
    # Após receber a msg ele a retorna junto com o nome da classe
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    

if __name__ == '__main__':
    l1 = LogFileMixin()
    l2 = LogPrintMixin()
    # Procura o metodo na classe LogFileMixin
    # Quando não encontra vai até a classe pai
    l1.log_error('Erro File')  
    l1.log_success('Success File')
    # l2.log_error('Erro Print')  
    # l2.log_success('Success Print')
  