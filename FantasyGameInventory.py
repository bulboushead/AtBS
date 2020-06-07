def displayInventory(inputInventory):

    print('Inventory: ')
    itemTotal = 0

    for k in inputInventory.items():
        print(str(k[1]) + ' ' + k[0])
        itemTotal += k[1]
    print('')
    print('Total number of items: ' + str(itemTotal))

def addToInventory(inventory, addedItems):
    # your code goes here
    for i in dragonLoot:
        inv.setdefault(i,0)
        inv[i] += 1

    return inv

inv =  {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

#stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
#displayInventory(stuff)