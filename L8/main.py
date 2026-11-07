from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

print("=== Section 2: Association ===")
supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Python eBook", 25.00, 100, 15.0,supplier)  # match your DigitalProduct params

laptop.supplier.display_information()
ebook.supplier.display_information()

del supplier
print("After del supplier:")
laptop.supplier.display_information()
print("Supplier and product are separate objects:", laptop is not laptop.supplier)