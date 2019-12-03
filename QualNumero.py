# Jogo qual eh o numero

# Importa a biblioteca de randomicos
import random

# Cria um numero secreto entre 1 e 20
secretNumber = random.randint(1, 20)
print('Eu estou pensando em um numero entre 1 e 20.')

# Pergunta ao jogar o numero, seis vezes
for guessesTaken in range(1, 7):
    print('Fale um numero')
    guess = int(input())

    if guess < secretNumber:
        print('Pouco..')
    elif guess > secretNumber:
        print('Muito..')
    else:
        break # Se ele acertar sai do Loop

if guess == secretNumber:
    print('Booooa, voce conseguiu depois de tentar ' + str(guessesTaken) + ' vezes!')
else:
    print('Nao consegue.... Moises, o numero era ' + str(secretNumber))
