# Esse programa diz ola e pergunta meu nome

print("Ola mundo!!")
print("Qual o seu primeiro nome?")
meuNome = input() # Salva o texto digitado
print("Prazer em conhece-lo " + meuNome)
print("O seu nome tem " + str(len(meuNome)) + " letras") # Mostra a quantidade de caracteres do nome informado
print("Quantos anos voce tem?")
minhaIdade = input() # Salva o texto digitado
print("Voce vai ter " + str(int(minhaIdade) + 1) + " no ano que vem") # Converte o valor em inteiro e faz uma soma