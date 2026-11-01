from product import Product


class DigitalProduct(Product):

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        # The parent prints the common fields, the child only adds its own
        super().display_information()
        print(f"Download Size: {self.__download_size} MB")
    def get_fulfilment_info(self):
        return "This product is delivered digitally."