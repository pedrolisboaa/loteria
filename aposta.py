from random import sample


class Aposta:
    def __init__(self, qtd_jogos=1):
        self.qtd_jogos = qtd_jogos

    def unico_jogo(self):
        jogo = sample(self.NUMEROS, 6)
        jogo.sort()
        return jogo

    def varios_jogos(self, qtd_jogos):
        todos_jogos = []
        for n in range(qtd_jogos):
            todos_jogos.append(self.unico_jogo())
        return todos_jogos

    def valor_total(self, qtd_jogos):
        return self.PRECO * qtd_jogos
