# Inventario
stuff = {'Corda': 1, 'Tocha': 6, 'moeda de ouro': 42, 'Punhal': 1, 'Flecha': 12} # Array com dados para teste

# Funcao para mostrar o inventario
def display_inventory(inventory):
    print("Inventario:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Numero total de itens: " + str(item_total))

display_inventory(stuff)