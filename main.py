from mega import Mega
from facil import Facil
from quina import Quina

print('-' * 30)
print(f'Bem vindo ao sorteio de jogos!')
print('-' * 30)
print()

while True:
    qtd_jogos = input('Informe quantos jogos deseja realizar: ')
    modalidade = input('Informe qual jogo deseja realizar [M]EGA, [F]ACIL, [Q]UINA: ').lower()

    if qtd_jogos.isdigit() and modalidade in ['m', 'f', 'q']:
        qtd_jogos = int(qtd_jogos)
        break
    else:
        if not qtd_jogos.isdigit():
            print(f'Você deve digitar um número inteiro positivo:')
        if not modalidade in ['m', 'f', 'q']:
            print(f'Você deve digitar "M", "F" ou "Q":')


if modalidade == 'm':
    jogo = Mega(qtd_jogos)
elif modalidade == 'f':
    jogo = Facil(qtd_jogos)
elif modalidade == 'q':
    jogo = Quina(qtd_jogos)

print()
print(f'Valor total R$ {jogo.valor_total(qtd_jogos):.2f}')
print(f'Seus jogos foram: ')
todos_jogos = jogo.varios_jogos(qtd_jogos)
for jogo in todos_jogos:
    print(*jogo)


