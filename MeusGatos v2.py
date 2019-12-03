nomeGatos = [] # Cria um vetor para salvar os nomes
# Cria um loop para pegar os valores
while True:
    print('Informe o nome de um gato ' + str(len(nomeGatos) + 1) + ' (Ou aperte enter para sair):')
    nome = input()
    if nome == '':
        break # Sai do loop caso seja apertado apenas ENTER
    nomeGatos = nomeGatos + [nome]  # Adiciona valor ao vetor
print('Os nomes deles sao: ')
for nome in nomeGatos:
    print('  ' + nome) # Exibe todos os nomes
