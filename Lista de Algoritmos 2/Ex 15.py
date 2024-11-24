#exercicio 15
import random
def jogo_adivinhacao ():
    numero_secreto = random.randint (1, 100)

    tentativas = 0
    acertou = False
    print ('Bem-vindo ao jogo de adivinhação!')
    print ('Eu escolhi um número entre 1 e 100. Tente adivinhar!')

    while not acertou:
        palpite = int (input('Digite o seu palpite:'))
        tentativas += 1
    
        if palpite < numero_secreto:
            print('O número secreto é maior. Tente novamente.')
    
        elif palpite > numero_secreto:
            print ('O número secreto é menor. Tente novamente.')
    
        else:
            acertou = True
            print(f'Parabéns! Você acertou o número {numero_secreto} em {tentativas}')
jogo_adivinhacao()

