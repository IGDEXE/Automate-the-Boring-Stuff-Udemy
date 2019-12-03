import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Inicia o programa')

def factorial(n):
    logging.debug('Inicia o factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i eh ' + str(i) + ', Total ' + str(total))
    return total
    logging.debug('Fim do factorial(%s%%)' % (n))

print(factorial(5))
logging.debug('Concluido')