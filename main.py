from itertools import combinations

class Item:
    def __init__(self, name, symbol, size, points):
        self.name = name
        self.symbol = symbol
        self.size = size
        self.points = points

items = [
    Item("Rifle", "r", 3, 25),
    Item("Pistol", "p", 2, 15),
    Item("Ammo", "a", 2, 15),
    Item("Medkit", "m", 2, 20),
    Item("Inhaler", "i", 1, 5),
    Item("Knife", "k", 1, 15),
    Item("Axe", "x", 3, 20),
    Item("Talisman", "t", 1, 25),
    Item("Flask", "f", 1, 15),
    Item("Antidote", "d", 1, 10),
    Item("Supplies", "s", 2, 20),
    Item("Crossbow", "c", 2, 20),
]

start_points = 10
bag_size = 9
grid_size = 3
max_points = sum(item.points for item in items)

def find_combinations(items, max_size, start_points):
    all_combinations = []
    for i in range(1, len(items) + 1):
        for combo in combinations(items, i):
            total_size = sum(item.size for item in combo)
            total_points = sum(item.points for item in combo)
            points_after_adjustment = total_points - (max_points - total_points) + start_points

            if total_size <= max_size and points_after_adjustment > 0:
                all_combinations.append((combo, points_after_adjustment))
    return all_combinations

combinations_found = find_combinations(items, bag_size, start_points)

def print_inventory(combinations_found):
    for combo, points in combinations_found:
        print("Combination:")
        inventory = []
        for item in combo:
            inventory.extend([item.symbol] * item.size)

        while len(inventory) < bag_size:
            inventory.append(" ")

        for i in range(0, len(inventory), grid_size):
            print(f"[{inventory[i]}],[{inventory[i + 1]}],[{inventory[i + 2]}]")

        print(f"Survival points: {points}")

print_inventory(combinations_found)
