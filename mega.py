from aposta import Aposta


class Mega(Aposta):
    NUMEROS = list(range(1, 61))
    PRECO = 4.50

    def __init__(self, qtd_jogos=1):
        super().__init__(qtd_jogos=1)
        self.qtd_jogos = qtd_jogos
