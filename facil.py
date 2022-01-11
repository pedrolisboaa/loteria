from aposta import Aposta


class Facil(Aposta):
    NUMEROS = list(range(1, 26))
    PRECO = 2.50

    def __init__(self, qtd_jogos=1):
        super().__init__(qtd_jogos=1)
        self.qtd_jogos = qtd_jogos


