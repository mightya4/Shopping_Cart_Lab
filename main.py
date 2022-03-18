from customer import Customer
from product import Product

customer1 = Customer("Chad")
print(customer1.name)

product1 = Product("Broccoli", 4.25, "Vegetable")
product2 = Product("Spring Water, 24 pk", 16.45, "Water")
product3 = Product("Ground Beef", 5.48, "Meat")


customer1.add_new_product(product2)
customer1.add_new_product(product1)
customer1.add_new_product(product3)

customer1.view_shopping_cart()

customer1_total_items = customer1.shopping_cart.total_of_products()
print(customer1_total_items)