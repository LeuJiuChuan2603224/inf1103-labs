import contextlib
import io
import os
import tempfile
import unittest

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from inventory_manager import load_inventory, save_inventory


def captured_display(product):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        product.display_information()
    return output.getvalue()


class TestProducts(unittest.TestCase):

    def setUp(self):
        self.guitar = PhysicalProduct("P1", "Guitar", 299.90, 5, 3.5)
        self.os = DigitalProduct("D1", "Operating System", 129.00, 100, 4096)

    def test_physical_displays_common_info_and_weight(self):
        output = captured_display(self.guitar)
        self.assertIn("ID: P1, Name: Guitar, Price: $299.90, Stock: 5", output)
        self.assertIn("Weight: 3.5 kg", output)

    def test_digital_displays_common_info_and_download_size(self):
        output = captured_display(self.os)
        self.assertIn("ID: D1, Name: Operating System, Price: $129.00, Stock: 100", output)
        self.assertIn("Download Size: 4096 MB", output)

    def test_both_subclasses_implement_fulfilment_info(self):
        self.assertIn("physical shipping", self.guitar.get_fulfilment_info())
        self.assertIn("digitally", self.os.get_fulfilment_info())

    def test_product_cannot_be_instantiated(self):
        with self.assertRaises(TypeError):
            Product("X1", "Generic", 1.00, 1)

    def test_shipping_cost_depends_on_weight(self):
        light = PhysicalProduct("P2", "Picks", 5.00, 10, 1)
        heavy = PhysicalProduct("P3", "Amp", 500.00, 2, 10)
        self.assertEqual(light.calculate_shipping_cost(), 7.00)
        self.assertEqual(heavy.calculate_shipping_cost(), 25.00)

    def test_only_physical_products_can_be_shipped(self):
        self.assertIsInstance(self.guitar, CanBeShipped)
        self.assertNotIsInstance(self.os, CanBeShipped)
        self.assertFalse(hasattr(self.os, "calculate_shipping_cost"))

    def test_inventory_operations(self):
        inventory = Inventory()
        inventory.add_product(self.guitar)
        inventory.add_product(self.os)
        self.assertIs(inventory.search_product("D1"), self.os)
        self.assertIsNone(inventory.search_product("nope"))
        self.assertTrue(self.guitar.update_stock(9))
        self.assertEqual(self.guitar.get_stock(), 9)
        self.assertFalse(self.guitar.update_stock(-1))
        self.assertEqual(self.guitar.get_stock(), 9)

    def test_json_preserves_product_types(self):
        inventory = Inventory()
        inventory.add_product(self.guitar)
        inventory.add_product(self.os)
        loaded = Inventory()
        start_dir = os.getcwd()
        with tempfile.TemporaryDirectory() as folder:
            os.chdir(folder)
            try:
                save_inventory(inventory)
                with contextlib.redirect_stdout(io.StringIO()):
                    load_inventory(loaded)
            finally:
                os.chdir(start_dir)
        guitar = loaded.search_product("P1")
        operating_system = loaded.search_product("D1")
        self.assertIsInstance(guitar, PhysicalProduct)
        self.assertEqual(guitar.get_weight(), 3.5)
        self.assertIsInstance(operating_system, DigitalProduct)
        self.assertEqual(operating_system.get_download_size(), 4096)


if __name__ == "__main__":
    unittest.main()