import contextlib
import inspect
import io
import os
import tempfile
import unittest
from unittest.mock import patch

from discount import (DiscountStrategy, NoDiscount, PercentageDiscount,
                      BulkDiscount, StudentDiscount)
from digital_product import DigitalProduct
from inventory import Inventory
from inventory_manager import get_positive_float
from order import Order, OrderLine
from physical_product import PhysicalProduct
from product_factory import ProductFactory
from product_loader import load_products
from supplier import Supplier


def run_quietly(function, *args):
    """Run a function and return everything it printed."""
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        function(*args)
    return output.getvalue()


class TestStrategy(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
        self.ebook = ProductFactory.create("digital", "D001", "Python eBook",
                                           25.00, 100, self.supplier, 15.0)

    def make_order(self, discount=None):
        order = Order("O001", discount)
        order.add_order_line(self.ebook, 10)   # 10 x 25 = 250
        return order

    def test_default_is_no_discount(self):
        order = self.make_order()
        self.assertIsInstance(order.discount, NoDiscount)
        self.assertEqual(order.calculate_total(), 250)

    def test_total_goes_through_strategy(self):
        self.assertEqual(self.make_order(BulkDiscount(200, 20)).calculate_total(), 230)
        self.assertEqual(self.make_order(PercentageDiscount(10)).calculate_total(), 225)

    def test_bulk_not_applied_below_threshold(self):
        self.assertEqual(BulkDiscount(200, 20).apply(150), 150)

    def test_set_discount_changes_total(self):
        order = self.make_order(BulkDiscount(200, 20))
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)

    def test_new_strategy_works_without_changing_order(self):
        order = self.make_order(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)

    def test_order_has_no_discount_if_elif(self):
        source = inspect.getsource(Order.calculate_total)
        self.assertNotIn("elif", source)
        self.assertNotIn("discount_type", source)

    def test_discount_strategy_is_abstract(self):
        with self.assertRaises(TypeError):
            DiscountStrategy()


class TestFactory(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")

    def test_creates_physical_product(self):
        product = ProductFactory.create("physical", "P001", "Laptop", 1200.0, 10, self.supplier, 2.5)
        self.assertIsInstance(product, PhysicalProduct)
        self.assertEqual(product.get_weight(), 2.5)

    def test_creates_digital_product(self):
        product = ProductFactory.create("digital", "D001", "eBook", 25.0, 100, self.supplier, 15.0)
        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_type_raises_clear_error(self):
        with self.assertRaises(ValueError) as context:
            ProductFactory.create("service", "S001", "Installation", 30.0, 5, self.supplier)
        self.assertIn("Unknown product type: service", str(context.exception))


class TestValidation(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")

    def test_price_must_be_positive(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P1", "Bad", 0, 5, self.supplier, 1.0)
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D1", "Bad", -10, 5, self.supplier, 1.0)

    def test_stock_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P1", "Bad", 10.0, -1, self.supplier, 1.0)

    def test_order_quantity_must_be_positive(self):
        product = ProductFactory.create("physical", "P1", "Lamp", 10.0, 5, self.supplier, 1.0)
        with self.assertRaises(ValueError):
            OrderLine(product, 0)
        with self.assertRaises(ValueError):
            Order("O1").add_order_line(product, -2)


class TestUserInput(unittest.TestCase):

    def test_keeps_asking_until_valid(self):
        # Pretend the user types abc, then -5, then 12.50
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                value = get_positive_float("Price: ")
        self.assertEqual(value, 12.50)
        self.assertIn("Please enter a valid number", output.getvalue())
        self.assertIn("Please enter a number greater than zero", output.getvalue())


class TestLoadProducts(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier("S001", "Acme Ltd", "sales@acme.com")
        self.inventory = Inventory()

    def test_missing_file_handled(self):
        output = run_quietly(load_products, "no_such_file.csv", self.inventory, self.supplier)
        self.assertIn("Products file not found", output)
        self.assertIn("Load attempt finished.", output)
        self.assertEqual(len(self.inventory.get_products()), 0)

    def test_bad_rows_skipped_good_rows_loaded(self):
        rows = ("product_type,product_id,name,price,stock_quantity\n"
                "physical,P001,Desk Lamp,25.00,10\n"
                "digital,D001,Photo Editor,49.90,100\n"
                "service,S001,Installation,30.00,5\n"
                "physical,P002,Office Chair,abc,3\n"
                "physical,P003,Monitor Stand,39.50,7\n")
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "products.csv")
            with open(path, "w", newline="") as file:
                file.write(rows)
            output = run_quietly(load_products, path, self.inventory, self.supplier)
        self.assertEqual(len(self.inventory.get_products()), 3)
        self.assertIn("Unknown product type: service", output)
        self.assertIn("could not convert string to float", output)
        self.assertIn("3 products loaded.", output)
        self.assertIn("Load attempt finished.", output)


if __name__ == "__main__":
    unittest.main()