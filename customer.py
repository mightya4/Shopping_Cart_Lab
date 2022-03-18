from shopping_cart import ShoppingCart
class Customer:
    def __init__(self, name):
        self.name = name
        self.shopping_cart = ShoppingCart()
    
    def add_new_product(self):
        self.shopping_cart.add_new_product()

    def view_shopping_cart(self):
        for item in self.shopping_cart.products:
            print("You have {item} in your shopping cart")

    