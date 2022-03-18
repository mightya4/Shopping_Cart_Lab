class ShoppingCart:
    def __init__(self):
        self.products = []

    def total_of_products(self):
        self.total = len(self.products)
        return self.total

    def add_new_product(self, product):
        self.products.append(product)

    def empty_all_products(self):
        del self.products
