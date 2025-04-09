def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item in inventory:
        total_items += inventory[item]
        print(f"{inventory[item]} {item}")
    
    print(f"Total number of items: {total_items}")

# List to Dictionary Function for Fantasy Game Inventory

def add_to_inventory(inventory, add_items):
    for item in add_items:
        if item in inventory.keys():
            inventory[item] +=1
        else:
            inventory[item] = 1
    
    return inventory

if __name__ == "__main__":
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    add_to_inventory(inv, dragonLoot)
    display_inventory(inv)