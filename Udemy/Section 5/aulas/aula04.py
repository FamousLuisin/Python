# Tem como manipular e tratar os dados dentros das instancias

class Camera:
    def __init__(self, modelo, filmando = False):
        self.modelo = modelo
        self.filmando = filmando

    def filmar(self):
        if self.filmando is True:
            print(f'{self.modelo} JÁ esta filmando...')
            return

        print(f'{self.modelo} esta filmando...')
        self.filmando = True

    def parar_filmar(self):
        if not self.filmando:
            print(f'Não esta filmando')
            return
        
        print(f'Parar Gravação')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'Não pode fotografar enquanto filma')
            return
        
        print(f'{self.modelo} esta fotografando...')

sony = Camera('Sony')
canon = Camera('Canon')

sony.parar_filmar()
sony.filmar()
sony.fotografar()
sony.parar_filmar()
sony.fotografar()

