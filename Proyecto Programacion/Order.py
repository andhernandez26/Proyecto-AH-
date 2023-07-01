from Client import Client
from Product import Product

class Order: 

    def __init__(self, param_client: Client, param_cart: list[dict[Product, int]], param_payment_method: str, param_delivery_method: str):
        self.client = param_client
        self.cart = param_cart
        self.payment_method = param_payment_method
        self.delivery_method = param_delivery_method
        self.subtotal = 0 
        self.discount = 0
        self.iva = 0
        self.igtv = 0
        self.total = 0

