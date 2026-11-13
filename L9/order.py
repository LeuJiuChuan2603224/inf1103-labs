from product import Product
from discount import DiscountStrategy, NoDiscount


class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.product: Product = product
        self.quantity: int = quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []
        # If no discount is given, use NoDiscount
        if discount is None:
            discount = NoDiscount()
        self.discount: DiscountStrategy = discount

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        self.order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> None:
        for line in self.order_lines:
            if line.product.get_product_id() == product_id:
                self.order_lines.remove(line)
                return

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)

    def display_order(self) -> None:
        print(f"Order {self.order_id}")
        for line in self.order_lines:
            print(f"  {line.product.get_name()} x{line.quantity} = ${line.calculate_subtotal():.2f}")
        print(f"  Total: ${self.calculate_total():.2f}")

        