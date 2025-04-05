from random import randint  # <-- AQUI COM 'N' !!!

N = 0
PONTOS_IA1 = 0
PONTOS_IA2 = 0

while N < 10:
    numero_escolhido_IA1 = randint(1, 10)
    numero_escolhido_IA2 = randint(1, 10)

    print(f'Numero escolhido por IA 1: {numero_escolhido_IA1}')
    print(f'Numero escolhido por IA 2: {numero_escolhido_IA2}')

    if numero_escolhido_IA1 == numero_escolhido_IA2:
        print('Empate')
    elif numero_escolhido_IA1 > numero_escolhido_IA2:
        print('Ponto para IA 1')
        PONTOS_IA1 += 1
    else:
        print('Ponto para a IA 2')
        PONTOS_IA2 += 1

    print(f'Pontos IA 1: {PONTOS_IA1}')
    print(f'Pontos IA 2: {PONTOS_IA2}\n')
    N += 1

print('\nPontuação Final:')
print(f'Pontos IA 1: {PONTOS_IA1}')
print(f'Pontos IA 2: {PONTOS_IA2}')