from discount import NoDiscount, PercentageDiscount, BulkDiscount
from discount import BulkDiscount, PercentageDiscount
from order import Order

from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from product import Product
from discount import StudentDiscount

supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
laptop = PhysicalProduct("P001", "Laptop", 1200.00, 10, 2.5, supplier)
ebook = DigitalProduct("D001", "Python eBook", 25.00, 100, 15.0,supplier)  

print(NoDiscount().apply(250))            # 250
print(PercentageDiscount(10).apply(250))  # 225.0
print(BulkDiscount(200, 20).apply(250))   # 230
print(BulkDiscount(200, 20).apply(150))   # 150 



print("=== Lab 9 Section 2: Strategy ===")
order3 = Order("O003", BulkDiscount(200, 20))
order3.add_order_line(ebook, 10)
print("Bulk discount total:", order3.calculate_total())

order3.set_discount(PercentageDiscount(10))
print("Percentage discount total:", order3.calculate_total())

order4 = Order("O004")   # no discount given
order4.add_order_line(ebook, 10)
print("No discount total:", order4.calculate_total())


order3.set_discount(StudentDiscount())
print("Student discount total:", order3.calculate_total())