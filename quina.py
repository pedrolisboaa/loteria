from aposta import Aposta


class Quina(Aposta):
    NUMEROS = list(range(1, 81))
    PRECO = 2

    def __init__(self, qtd_jogos=1):
        super().__init__(qtd_jogos=1)
        self.qtd_jogos = qtd_jogos


