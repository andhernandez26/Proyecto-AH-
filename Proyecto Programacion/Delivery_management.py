from Delivery import Delivery
from Client import Client
from Client_management import Client_management
from Client_natural import Client_natural 
from Client_juridico import Client_juridico
from utils import get_date

class Delivery_management:
    def __init__(self):
        self.deliveries = []
        self.clients = []

    def register_delivery(self):
        """
    Registra un nuevo servicio de entrega asociado a un cliente.

    Solicita al usuario ingresar la cédula o RIF del cliente. Luego, verifica si existe un cliente con esa identificación en la lista de clientes.
    Si el cliente existe, se solicita al usuario ingresar el tipo de envío deseado, que puede ser:
    - 1: MRW
    - 2: Zoom
    - 3: Delivery

    Si se selecciona "Delivery" como tipo de envío, se solicita al usuario ingresar información adicional del motorizado, como el nombre, la cédula de identidad y el número telefónico.

    Finalmente, se registra la entrega con la información proporcionada y se agrega a la lista de entregas.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        info_moto = {}
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
        
            service = input("Ingrese el tipo de envio que desea obtener \n1. MRW \n2. Zoom \n3. Delivery \n")
            while not service.isnumeric() or service not in ["1", "2", "3"]:
                service = input("Ingrese un valor valido: ")
            if service == "1":
                service = "MRW"
            elif service == "2":
                service = "Zoom"
            else:
                service = "Delivery"
                name_moto = input("Ingrese el nombre del motorizado: ").title()
                id_moto = input("Ingrese la cedula de identidad: ")
                phone_moto = input("Ingrese el numero telefonico: ")
                info_moto = {"name": name_moto, "ID": id_moto, "Telefono": phone_moto}
            date = get_date()
            delivery = Delivery(n, date, service, info_moto)
            self.deliveries.append(delivery)
            
        else: 
            print("No existe un cliente asociado con esta cedula o RIF")

        return delivery
    
    def filter_client(self):
        """
    Filtra y muestra los servicios de entrega asociados a un cliente específico.

    Solicita al usuario ingresar la cédula o RIF del cliente. Luego, itera sobre la lista de entregas y compara la identificación del cliente asociado a cada entrega con la identificación ingresada por el usuario.
    Si encuentra una coincidencia, muestra los detalles de la entrega mediante el método `show_delivery()`.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        id = input("Ingrese la cedula o rif: ")
        for delivery in self.deliveries:
            if delivery.client.id == id or delivery.client.rif == id:
                print(delivery.show_delivery())
    
    def filter_date(self):
        """
    Filtra y muestra los servicios de entrega asociados a una fecha específica.

    Obtiene la fecha actual utilizando el método `get_date()`. Luego, itera sobre la lista de entregas y compara la fecha de cada entrega con la fecha obtenida.
    Si encuentra una coincidencia, muestra los detalles de la entrega mediante el método `show_delivery()`.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        date = get_date()
        for delivery in  self.deliveries:
            if delivery.date == date:
                print(delivery.show_delivery())

    def menu_deliveries(self):
        
        while True: 
            option = input("""
--- Menu de envios --- 

1. Registrar envio
2. Buscar envio
3. Regresar
                 
""")     
            while not option.isnumeric() or option not in ["1", "2", "3"]:
                option = input("Ingrese un valor valido: ")

            if option == "1":
                self.register_delivery()
            elif option == "2":
                while True: 
                    option_1 = input("""
---- Menu de busqueda ---

1. Por cliente
2. Por fecha
3. Regresar
                     
""")
                    while not option_1.isnumeric() or option_1 not in ["1", "2", "3"]:
                        option_1 = input("Ingrese un valor valido: ")
                    
                    if option_1 == "1":
                        self.filter_client()
                    elif option_1 == "2":
                        self.filter_date()
                    else: 
                        break

            else:
                break