import random
heads = 0
tails = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads = heads + 1
    else:
        tails = tails + 1
    if i == 500:
        print('Chegamos na metade!')
print('Cara caiu ' + str(heads) + ' vezes.')
print('Coroa caiu ' + str(tails) + ' vezes.')
