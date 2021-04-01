# Madison Fletcher
# 1868748
class ItemToPurchase:

    def __init__(self, item_name="none", item_quantity=0, item_price=0, item_description='none'):
        self.item_name = item_name
        self.item_quantity = item_quantity
        self.item_price = item_price
        self.item_description = item_description

    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", '${}'.format(self.item_price), "=",
              '${}'.format(self.item_quantity * self.item_price))

    def print_item_description(self):
        print("{}: {}".format(self.item_name, self.item_description))


class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, cartItem):
        self.cart_items.append(cartItem)

    def remove_item(self, item_name):
        count = 0
        items = self.cart_items[:]
        for i in range(len(items)):
            i = items[i]
            if item_name == item_name:
                del self.cart_items[i]
                count += 1

        if count == 0:
            print(" ")
            print("Item not found in cart. Nothing removed.")

    def modify_item(self):
        print('CHANGE ITEM QUANTITY')
        name = str(input('Enter the item name: '))
        flag = True
        for item in self.cart_items:
            if item.item_name == name:
                flag = False
                quantity = int(input('Enter the new quantity: '))
                item.item_quantity = quantity
                break
            if not flag:
                print('Item not found in cart. Nothing modified')

    def get_num_items_in_cart(self):
        num = 0
        for x in self.cart_items:
            num = num + x.item_quantity
        return num

    def get_cost_of_cart(self):
        count = 0
        for y in self.cart_items:
            cost = (y.item_quantity * y.item_price)
            count = count + cost
        return count

    def print_total(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        count = len(self.cart_items)
        if count == 0:
            print(" ")
            print("SHOPPING CART IS EMPTY")
            return 0

        print("Number of Items: " + str(count))
        print(" ")

        for itm in self.cart_items:
            itm.print_item_cost()

        total = self.get_cost_of_cart()
        print("Total: $", total)

    def print_descriptions(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print(" ")
        print("Item Descriptions")

        for itm in self.cart_items:
            print(itm.item_name() + ": " + itm.item_description())


def print_menu():
    print(" ")
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print(" ")
