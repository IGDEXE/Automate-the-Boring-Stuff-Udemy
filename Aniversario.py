aniversarios = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Informe um nome: (Apenas enter para encerrar)')
    nome = input()
    if nome == '':
        break

    if nome in aniversarios:
        print(aniversarios[nome] + ' eh o aniversario de ' + nome)
    else:
        print('Nao tenho informacoes sobre ' + nome)
        print('Quando eh o aniversario?')
        bday = input()
        aniversarios[nome] = bday
        print('Aniversario cadastrado.')
