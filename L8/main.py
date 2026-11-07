from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product

print("=== Section 2: Association ===")
supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Python eBook", 25.00, 100, 15.0,supplier)  

laptop.supplier.display_information()
ebook.supplier.display_information()

del supplier
print("After del supplier:")
laptop.supplier.display_information()
print("Supplier and product are separate objects:", laptop is not laptop.supplier)

print("=== Section 3: Aggregation ===")
inventory_a = Inventory()
inventory_b = Inventory()
inventory_a.add_product(laptop)
print("In A:", inventory_a.find_product("P001") is not None)
inventory_a.remove_product("P001")
print("In A after remove:", inventory_a.find_product("P001") is not None)
laptop.display_information()
inventory_b.add_product(laptop)
print("Same object in B:", inventory_b.find_product("P001") is laptop)

print("=== Section 4: Composition ===")
order1 = Order("O001")
order1.add_order_line(laptop, 2)
order1.add_order_line(ebook, 1)
order1.display_order()
order2 = Order("O002")
order2.add_order_line(laptop, 1)
line_1 = order1.order_lines[0]
line_2 = order2.order_lines[0]
print("Same OrderLine?", line_1 is line_2)
print("Same Product?", line_1.product is line_2.product)
order1.remove_order_line("D001")
order1.display_order()

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

print("=== Section 6: LSP ===")
show_product_details(laptop)
show_product_details(ebook)
lsp_inventory = Inventory()
lsp_inventory.add_product(laptop)
lsp_inventory.add_product(ebook)
lsp_inventory.display_all()

print("=== Section 7: Polymorphism ===")
shop = Inventory()
shop.add_product(laptop)
shop.add_product(ebook)

for product in shop.get_products():
    product.display_information()
    print(product.get_fulfilment_info())