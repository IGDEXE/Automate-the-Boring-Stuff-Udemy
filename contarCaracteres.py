message = 'Salve o Corinthians, campeao dos campeoes.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# Mostra a contagem
print(count)
