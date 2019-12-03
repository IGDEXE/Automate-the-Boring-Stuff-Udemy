# Funcao para desenhar quadrados
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('O simbolo precisa ser um caracter unico.')
    if width <= 2:
        raise Exception('A largura precisa ser maior que 2.')
    if height <= 2:
        raise Exception('A altura precisa ser maior que 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# Faz o desenho
for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('Um problema aconteceu: ' + str(err))
