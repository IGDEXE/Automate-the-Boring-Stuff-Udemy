import time
startTime = time.time()
# Calcula o produto dos 100 Mil primeiro numeros
product = 1
for i in range(1, 100000):
    product = product * i
endTime = time.time()
print('Total de %s digitos.' % (len(str(product))))
print('Levou %s segundos para calcular.' % (endTime - startTime))
