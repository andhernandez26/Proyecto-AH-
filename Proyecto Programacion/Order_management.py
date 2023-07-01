from Order import Order
from Product import Product
from Client import Client
from Client_management import Client_management
from Payment_management import Payment_management
from Client_natural import Client_natural 
from Delivery_management import Delivery_management
from Client_juridico import Client_juridico
from Payment import Payment
import datetime

# menu recibe delivery_management
# menu recibe payment_management

class Order_management:
    def __init__(self):
        self.order  = []
        self.products = []
        self.clients = []
        self.delivery_management = None
        self.payment_management = None
    
    def register_order(self):
        """
    Registra una nueva orden de compra.

    Solicita al usuario ingresar la cédula o RIF del cliente.
    Busca el cliente en la lista de clientes y determina si es de tipo natural o jurídico.
    Si se encuentra un cliente válido, se procede a llenar el carrito de compras.
    El usuario selecciona los productos y las cantidades deseadas.
    Luego se solicita el método de entrega, creando un objeto de envío utilizando el método `register_delivery()`.
    Se calcula el subtotal de la orden, considerando el carrito de compras.
    Si el cliente es de tipo jurídico, se pregunta si desea pagar de contado.
    En caso afirmativo, se establece el tipo de cliente como "juridico_contado" y se aplica un descuento del 5% al subtotal.
    Si el cliente no es de tipo jurídico de contado, se solicita el método de pago, creando un objeto de pago utilizando el método `register_payment()`.
    Luego se crea la orden de compra utilizando la información recopilada.
    La orden se agrega a la lista de órdenes existentes.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        # variables
        n = None
        client_type = "natural"
        subtotal = 0
        discount = 0 
        iva = 0 
        igtf = 0 
        total = 0 

        # buscar cliente
        option = input("Ingrese la cedula o rif: ")
        for client in self.clients:
            print(client.id)
            print(client.rif)
            if isinstance(client, Client_natural):
                if option.lower() == client.id.lower():
                    n = client
            else:
                if option.lower() == client.rif.lower():
                    n = client
                    client_type = "juridico"
        if not n == None:
            # llenar carrito
            cart = {} 
            while True: 
                for i, product in enumerate(self.products): 
                    print(f'{i+1}, {product.show_product()}')
                option = input("Ingrese la opcion que desee: ")
                while not option.isnumeric() or not int(option) in range(1, len(self.products)+1):
                    option = input("Ingrese un valor valido: ")
                amount = input("Ingrese la cantidad que desea del producto: ")
                while not amount.isnumeric() or int(amount) == 0 or int(amount)> self.products[int(option)-1].inventory:
                    amount = input("No se tiene dicha cantidad en stock. Ingrese un numero valido: ")
                cart[self.products[int(option)-1].name] = int(amount)
                otro = input("Dese agregar otro producto al carrito ('1' para si, '2' para no): ")
                while otro not in ["1", "2"]:
                    otro = input("Ingrese un valor valido: ")
                if otro == "1":
                    continue
                else:
                    break
            # crear envio
            delivery_method = self.delivery_management.register_delivery()


            # subtotal
            subtotal = self.get_subtotal(cart)


            # iva
            subtotal  *= 1.16
            
            if client_type == "juridico":
                contado = input("Desea pagar de contado ('1' para si, '2' para no): ")
                if contado == "1":
                    client_type == "juridico_contado"

            if client_type == "juridico_contado":
                # no se crea un pago, pero si una orden
                payment_method == None
                # descuento por pago de contado
                discount = subtotal * 0.05
                
            else:
                payment_method = self.payment_management.register_payment()        
            
                # igtf. calcular con payment_method.coin

                

            order = Order(client, cart, payment_method, delivery_method)
            self.order.append(order)
        else:
            print("No existe ningun cliente registrado con esta cedula o rif")

    def create_bill(self): 
        pass

    def get_subtotal(self, cart):
        """
    Calcula el subtotal de una compra en base al carrito de compras y los precios de los productos.

    Recorre el carrito de compras y busca cada producto en la lista de productos disponibles.
    Suma el precio del producto multiplicado por la cantidad en el carrito al subtotal.
    Retorna el subtotal calculado.

    Args:
        self: El objeto de la clase que invoca el método.
        cart (dict): Un diccionario que representa el carrito de compras, donde las claves son los nombres de los productos y los valores son las cantidades deseadas.

    Returns:
        float: El subtotal de la compra.

    """
        subtotal = 0
        for prod in self.products:
                if prod.name in list(cart.keys()):
                    subtotal += prod.name*cart[prod.name]
        return subtotal

    def get_discount(self, client_type, subtotal): # revisar
        """
    Calcula el descuento aplicable a una compra en base al tipo de cliente y el subtotal.

    Si el cliente es de tipo "juridico" y decide pagar de contado, se aplica un descuento del 5% sobre el subtotal.
    Si el cliente no es de tipo "juridico" o decide no pagar de contado, no se aplica ningún descuento.

    Args:
        self: El objeto de la clase que invoca el método.
        client_type (str): El tipo de cliente ("juridico" o cualquier otro).
        subtotal (float): El subtotal de la compra antes de aplicar descuentos.

    Returns:
        float: El valor del descuento aplicado (0 si no aplica descuento).

    """
        if client_type == "juridico":
                contado = input("Desea pagar de contado ('1' para si, '2' para no): ")
                if contado == "1":
                    return subtotal * 0.05
                else:
                    return 0 
        
    def get_IGTF(self):
        """
    Calcula el monto del Impuesto a las Grandes Transacciones Financieras (IGTF) aplicable a una compra.

    Si el método de pago es en dólares, se aplica un IGTF del 3% sobre el subtotal de la compra.
    Si el método de pago no es en dólares, no se aplica IGTF.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        float: El monto del IGTF aplicado (0 si no aplica IGTF).

    """
        if self.payment_method == "dolar":
            return self.subtotal * 0.03
        else:
            return 0 

    def menu_orders(self):
        while True:
            option = input("""
--- Menu de ventas --- 

1. Registrar venta
2. Generar factura
3. Buscar
4. Regresar            
            
""")
            while not option in ["1", "2", "3", "4"]:
                option = input("Ingrese un valor valido: ")
            if option == "1":
                self.register_order()
            elif option == "2":
                pass
            elif option == "3":
                while True:
                    option_2 = input("""
--- Menu de busqueda ---

1. Por cliente
2. Por fecha de la venta
3. Monto total de la venta
4. Regresar                                     """) 
                    while not option_2 in ["1", "2", "3", "4"]:
                        option_2 = input("Ingrese una opcion valida: ")
                    if option_2 == "1":
                        pass
                    elif option_2 == "2":
                        pass
                    elif option_2 == "3":
                        pass
                    else: 
                        break
            else:
                break