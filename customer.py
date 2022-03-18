from shopping_cart import ShoppingCart
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()
    
    def add_new_product(self, product):
        self.shopping_cart.add_new_product(product)

    def view_shopping_cart(self):
        for item in self.shopping_cart.products:
            print(f"You have {item.name} in your shopping cart")

    