
from Product_management import Product_management
from Client_management import Client_management
from Payment_management import Payment_management
from Delivery_management import Delivery_management
from Order_management import Order_management
import requests
import pickle
import os

class App: 
    def __init__(self): 
        self.total_sales = []
        self.products = []
        self.clients = []
        self.deliveries = []
        self.payments = []
        self.product_management = None
        self.client_management = Client_management()
        self.payment_management = Payment_management()
        self.delivery_management = None
        self.order_management = None
    
    def api(self):
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json"
        response = requests.request("GET", url)
        return response.json()

    def load_txt(self, file):
        try:
            with open(file, "rb") as f: 
                return pickle.load(f)
        except EOFError:
            return []

    def write_txt(self, file, l):
        with open(file, "wb") as f:
            pickle.dump(l, f)

    def read_txt(self, archivo, lista):
        if os.path.getsize(archivo) > 0:
            with open(archivo, 'rb') as f:
                lista - pickle.load(f)
    
    def translate_txt(self, archivo, lista):
        with open(archivo, "wb") as f:
            pickle.dump(lista, f)

    def menu(self):

        self.product_management = Product_management()
        self.payment_management = Payment_management()
        self.delivery_management = Delivery_management()
        self.order_management = Order_management()
        self.clients = self.load_txt("clients.txt")
        self.payments = self.load_txt("payments.txt")
        self.orders = self.load_txt("orders.txt")
        self.deliveries = self.load_txt("deliveries.txt")
        self.delivery_management.deliveries = self.deliveries
        d = input("\nDesea descagar los productos de la api o leerlos de la base de datos local.\n\n1. Api \n2. Base de datos local \n")
        while not d in ['1', '2']:
            d = input("Ingrese un valor valido: ")
        if d == "1":
            self.products = self.product_management.register_products(self.api()) 
            self.write_txt('products.txt', self.products)

            # print(self.products)
        else: 
          self.products = self.load_txt("products.txt")
          if len(self.products) == 0:
              print("No hay informacion en la base de datos actual")
              self.products = self.product_management.register_products(self.api())
              self.write_txt('products.txt', self.products)
        #   print(self.products)
        
        print("""
        
                                                        ---------- Bienvenidos a la tienda ----------
        
        """)
        while True: 
            option = input('''
--Menu principal--

1. Gestion de productos
2. Gestion de ventas
3. Gestion de clientes
4. Gestion de pagos
5. Gestion de envios
6. Indicadores de gestion
7. Salir

''')
            while not option in ["1", "2", "3", "4", "5", "6", "7"]:
                option = input("Error! Ingrese un valor valido: ")

            if option == "1":
                self.product_management.menu_products(self.products)
            elif option == "2":
                self.order_management.menu_orders()
            elif option == "3":
                self.client_management.menu_clients()
                self.clients = self.client_management.clients
                self.write_txt("clients.txt", self.clients)
            elif option == "4":
                self.payment_management.menu_payments(self.clients)
                self.payments = self.payment_management.payments
                self.write_txt("payments.txt", self.payments)
            elif option == "5":
                self.delivery_management.menu_deliveries()
            elif option == "6":
                pass
            elif option == "7": 
                break

            another = input("\nDesea realizar otra operacion en el sistema? ('1' para sí, '2' para no): ")
            while not another in ["1", "2"]:
                another = input("Error! Ingrese un valor valido: ")
            if another == "1":
                continue
            else:
                break

    def start(self):
        self.menu()