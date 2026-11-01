from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P1", "Guitar", 299.90, 5, 3.5)
operating_system = DigitalProduct("D1", "Operating System", 129.00, 100, 4096)

guitar.display_information()
print()
operating_system.display_information()