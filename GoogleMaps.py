#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Recebe o endereco da linha de comando
    address = ' '.join(sys.argv[1:])
else:
    # Recebe o endereco da area de transferencia
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
