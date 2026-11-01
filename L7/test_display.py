from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P1", "Guitar", 299.90, 5, 3.5)
operating_system = DigitalProduct("D1", "Operating System", 129.00, 100, 4096)

# 2.2: display information
guitar.display_information()
print()
operating_system.display_information()
print()

# 3.2: fulfilment info
print(guitar.get_fulfilment_info())
print(operating_system.get_fulfilment_info())
print()

# 3.3: Product should be blocked
try:
    Product("X1", "Generic", 1.00, 1)
    print("Problem: Product was created")
except TypeError as error:
    print("Blocked:", error)
print()

# 4.2: shipping cost with different weights
# light = PhysicalProduct("P2", "Picks", 5.00, 10, 1)
# heavy = PhysicalProduct("P3", "Amp", 500.00, 2, 10)
# print(light.calculate_shipping_cost())
# print(heavy.calculate_shipping_cost())