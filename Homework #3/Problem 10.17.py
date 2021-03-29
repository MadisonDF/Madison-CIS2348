# Madison Fletcher
# 1868748
class ItemToPurchase:
    def __init__(self, item_name="none", item_quantity=0, item_price=0):
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_price = item_price

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", '${}'.format(self.item_price), "=",
              '${}'.format(self.item_quantity * self.item_price))


if __name__ == "__main__":
    print("Item 1")
    name = str(input("Enter the item name:\n"))
    price = int(input("Enter the item price:\n"))
    quantity = int(input("Enter the item quantity:\n"))

    items = ItemToPurchase(name, quantity, price)

    print("\nItem 2")
    name2 = str(input("Enter the item name:\n"))
    price2 = int(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))

    items2 = ItemToPurchase(name2, quantity2, price2)
    items3 = ItemToPurchase()

    print("\nTOTAL COST")
    items.print_item_cost()
    items2.print_item_cost()
    print("\nTotal:", '${}'.format(price * quantity + price2 * quantity2))
