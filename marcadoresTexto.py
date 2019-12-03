#! python3
# Adiciona marcadores do Wikipedia em cada linha de texto da area de transferencia

# importa a biblioteca necessaria
import pyperclip
# Pega o texto na area de transferencia
text = pyperclip.paste()

# Separa as linhas e adiciona marcadores
lines = text.split('\n')
for i in range(len(lines)): # Para cada linha dentro do texto
    lines[i] = '* ' + lines[i] # Adiciona um marcador no inicio dela
text = '\n'.join(lines)
pyperclip.copy(text)
