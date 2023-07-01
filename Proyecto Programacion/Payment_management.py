from Payment import Payment
from Client import Client
from Client_management import Client_management
from Client_natural import Client_natural 
from Client_juridico import Client_juridico
from utils import get_date


class Payment_management:
    def __init__(self):
        self.payments = []
        self.clients = []

    def register_payment(self):
        """
    Registra un pago asociado a un cliente.

    Solicita al usuario ingresar la cédula o RIF del cliente y busca en la lista de clientes si existe un cliente con ese identificador. Luego, solicita al usuario ingresar el monto del pago y la moneda del pago. Dependiendo de la moneda, se ofrecen diferentes opciones de tipo de pago. Finalmente, registra el pago con la información proporcionada, incluyendo la fecha del pago.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        n = None
    
        option = input("Ingrese la cedula o rif: ")
        for client in self.clients:
            if isinstance(client, Client_natural):
                if option.lower() == client.id.lower():
                    n = client
            else:
                if option.lower() == client.rif.lower():
                    n = client
            
        if not n == None: 
            while True:
                try: 
                    amount = float(input("\nIngrese el monto del pago: "))
                    break
                except:
                    print("Error! Ingrese valores validos ")
            coin = input("\nIngrese la moneda del pago: \n1. Bolivares \n2. Dolares \nOpcion: ")
            if coin == "1":
                coin = "Bolivar"
                payment_type = input("\nIngrese el tipo de pago: \n1. Cash \n2. Punto de venta \n3. Pago Movil \nOpcion: ")
                if payment_type == "1":
                    payment_type = "Cash"
                elif payment_type == "2":
                    payment_type = "Punto de venta"
                else:
                    payment_type = "Pago movil"
                print("\n-Fecha de pago-\n")
                date = get_date()

                print("\n\n--- Pago registrado con exito! ---\n")
                payment = Payment(n, amount, coin, payment_type, date)
                self.payments.append(payment)
            else: 
                coin = "Dolar"
                payment_type = input("\nIngrese el tipo de pago: \n1. Zelle \n2. Cash \n3. Punto de venta \nOpcion: ")
                if payment_type == "1":
                    payment_type = "Zelle"
                elif payment_type == "2":
                    payment_type = "Cash"
                else:
                    payment_type = "Punto de venta"
                print("\n-Fecha de pago-\n")
                date = get_date()

                print("\n\n--- Pago registrado con exito! ---\n")
                payment = Payment(n, amount, coin, payment_type, date)
                self.payments.append(payment)
           
        else: 
            print("No existe un cliente asociado con esta cedula o RIF")

    def filter_client(self):
        """
    Filtra y muestra los pagos asociados a un cliente específico.

    Solicita al usuario ingresar la cédula o RIF del cliente y busca en la lista de pagos si existen pagos asociados a ese cliente. Luego, muestra los detalles de los pagos encontrados.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        id = input("\nIngrese la cedula o rif: ")
        for payment in self.payments:
                if payment.client.id == id or payment.client.rif == id:
                    print(payment.show_payment())

    def filter_date(self):
        """
    Filtra y muestra los pagos realizados en una fecha específica.

    Solicita la fecha al usuario utilizando la función `get_date()`. Luego, busca en la lista de pagos si existen pagos realizados en esa fecha y muestra los detalles de los pagos encontrados.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        date = get_date()
        for payment in  self.payments:
            if payment.date == date:
                print(payment.show_payment())

    def filter_payment_method(self):
        """
    Filtra y muestra los pagos realizados utilizando un método de pago específico.

    Solicita al usuario ingresar el tipo de pago deseado, utilizando las siguientes abreviaturas:
    - Z: Zelle
    - C: Cash
    - PDV: Punto de Venta
    - PM: Pago Móvil

    Luego, busca en la lista de pagos si existen pagos realizados utilizando el método de pago seleccionado y muestra los detalles de los pagos encontrados.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        payment_type = input("\nIngrese el tipo de pago (Z = zelle)(C = cash)(PDV = Punto de Venta)(PM = Pago Movil): ").upper()
        if payment_type == "Z":
            payment_type = "Zelle"
        elif payment_type == "C":
            payment_type = "Cash"
        elif payment_type == "PDV":
            payment_type = "Punto de venta"
        elif payment_type == "PM":
            payment_type = "Pago movil"
        for payment in  self.payments:
            if payment.payment_type == payment_type:
                print(payment.show_payment())
    
    def filter_coin(self):
        """
    Filtra y muestra los pagos realizados en una moneda específica.

    Solicita al usuario ingresar la moneda de pago deseada utilizando las siguientes abreviaturas:
    - B: Bolívar
    - D: Dólar

    Luego, busca en la lista de pagos si existen pagos realizados en la moneda seleccionada y muestra los detalles de los pagos encontrados.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        coin = input("\nIngrese la moneda de pago (B = bolivar)(D = dolar): ").upper()
        if coin == "B":
            coin = "Bolivar"
        elif coin == "D":
            coin = "Dolar"
        for payment in  self.payments:
            if payment.coin == coin:
                print(payment.show_payment())
                    
    def menu_payments(self, clients):
          self.clients = clients
          while True: 
            option = input('''
--- Menu de pagos ---

1. Registrar
2. Buscar
3. Regresar

''')
            while not option in ["1", "2", "3"]:
                option = input("Error! Ingrese un valor valido: ")
    
            if option == "1":
                self.register_payment()
            elif option == "2": 
                while True: 
                    option_1 = input('''
--- Menu de busqueda ---

1. Cliente
2. Fecha
3. Tipo de pago
4. Moneda de pago
5. Regresar 

''')
                    while not option_1 in ["1", "2", "3", "4","5"]:
                        option_1 = input("Error! Ingrese un valor valido: ")

                    if option_1 == "1":
                        self.filter_client()
                    elif option_1 == "2":
                        self.filter_date()
                    elif option_1 == "3":
                        self.filter_payment_method()
                    elif option_1 == "4":
                        self.filter_coin()
                    elif option_1 == "5":
                        break
            else: 
                break   