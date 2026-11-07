from supplier import Supplier
from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    BASE_SHIPPING_COST :float= 5.00
    COST_PER_KG :float = 2.00

    def __init__(self, product_id:str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        # The parent prints the common fields, the child only adds its own
        super().display_information()
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self.BASE_SHIPPING_COST + self.COST_PER_KG * self.__weight

    def to_dict(self) -> dict :
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data