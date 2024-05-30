import random 

class Item:
    def __init__(self, id, size, value):
        self.id = id
        self.size = size
        self.value = value

def generate_items(no_items):
    items = []
    for i in range(no_items):
        size = random.randint(1, 50)
        value = random.randint(1, 50)
        items.append(Item(i, size, value))
    return items

def print_items(items):
    print("\nHomari disponibili:")
    for item in items:
        print(f"Homarul: {item.id}    Dimensiune: {item.size} cm    Valoare: {item.value} monede de aur")
    print()

def sort_items_by_value(items):
    items.sort(key=lambda x: x.value, reverse=True)

def greedy_lobster_selection(items, net_capacity):
    net_current_capacity = 0
    net_value = 0
    selected_items = []

    for item in items:
        if net_current_capacity + item.size <= net_capacity:
            net_current_capacity += item.size
            net_value += item.value
            selected_items.append(item.id)

    if selected_items:
        print("\nHomarii alesi de pescar sunt: ", end="")
        print(", ".join(map(str, selected_items)) + ".")
    else:
        print("Niciun homar.")

    print(f"\nValoarea crustaceului din plasa de pescuit: {net_value}")

def main():
    net_capacity = int(input("Capacitatea plasei: "))
    no_items = int(input("Nr de homari disponibili: "))

    items = generate_items(no_items)
    print("\n=== Homari disponibili ===")
    print_items(items)

    sort_items_by_value(items)
    print("\n=== Homari sortați după valoare ===")
    print_items(items)

    greedy_lobster_selection(items, net_capacity)

if __name__ == "__main__":
    main()
