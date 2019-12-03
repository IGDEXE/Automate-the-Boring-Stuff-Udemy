#! python3
# Pesquisar no Google

# Importa as bibliotecas necessarias
import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retorna os principais resultados
soup = bs4.BeautifulSoup(res.text)

# Abre no navegador a pagina
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
