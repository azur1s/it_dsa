class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_weight(self):
        return self.weight

def knapsack(items, capacity):
    xs = sorted(items, key=lambda x: x.get_price() / x.get_weight(), reverse=True)

    sack = []
    total = 0
    remaining = capacity
    for x in xs:
        if remaining - x.get_weight() < 0:
            break
        sack.append(x)
        total += x.get_price()
        remaining -= x.get_weight()

    print(f"Knapsack Size: {capacity} kg")
    print("===============================")
    for item in sack:
        print(f"{item.get_name()} -> {item.get_weight()} kg -> {item.get_price()} THB")

    print(f"Total: {total} THB")

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)

main()