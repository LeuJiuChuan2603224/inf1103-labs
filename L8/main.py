from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

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