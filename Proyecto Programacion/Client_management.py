from Client import Client
from Client_natural import Client_natural
from Client_juridico import Client_juridico
from Client_juridico import Client_juridico

class Client_management:
    def __init__(self):
        self.clients = []

    def register_clients(self):
        """
    Registra nuevos clientes en el sistema.

    Solicita al usuario ingresar los datos del cliente, como el nombre completo o nombre de la entidad, el tipo de cliente (natural o jurídico), y los detalles específicos según el tipo de cliente.
    Para clientes naturales, se solicita la cédula de identidad, el correo electrónico, la dirección y el teléfono celular.
    Para clientes jurídicos, se solicita el número de RIF, el correo electrónico de la entidad, la dirección y el teléfono de la entidad.
    Crea una instancia del cliente correspondiente (Cliente_natural o Cliente_juridico) con los datos proporcionados y lo agrega a la lista de clientes.
    Finalmente, muestra un mensaje de éxito y los detalles del nuevo cliente registrado.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        name = input("\nIngrese su nombre completo o nombre de la entidad: ").title()
        kind = input("\nSi usted es de tipo natural ingrese 'N'. Si es de tipo juridico ingrese 'J': ").upper()
        if kind == "N":
            id = input("\nIngrese su cedula de identidad sin espacios ni caracteres: ")
            while not id.isnumeric():
                id = input("Error! Ingrese un valor valido: ")
            email = input("\nIngrese el correo electronico: ")
            address = input("\nIngrese su direccion: ").title()
            phone = input("\nIngrese su telefono celular: ")
            while len(phone) < 11:
                phone = input("Error! Ingrese un valor valido: ")

            new_client = Client_natural(name, id, email, address, phone)
            self.clients.append(new_client)
        else: 
            id = input("\nIngrese su numero de RIF sin espacios ni caracteres: ")
            while not id.isnumeric() or not len(id) < 10:
                id = input("Error! Ingrese un valor valido: ")
            email = input("\nIngrese el correo electronico de la entidad: ")
            address = input("\nIngrese la direccion de la entidad: ").capitalize()
            phone = input("\nIngrese el telefono de la entidad: ")
            while len(phone) < 11:
                phone = input("Error! Ingrese un valor valido: ")

            new_client = Client_juridico(name, id, email, address, phone)
            self.clients.append(new_client)

        print("\n\n--- Cliente registrado con exito! ---\n")
        new_client.show_client()
#Modificar
    def modify_clients(self):
        """
    Modifica los datos de un cliente existente en el sistema.

    Muestra la lista de clientes disponibles y solicita al usuario ingresar el número del cliente que desea modificar.
    Luego, dependiendo del tipo de cliente (natural o jurídico), se le presenta un menú de opciones para seleccionar el dato específico que se desea modificar (nombre, ID, email, dirección, teléfono).
    El usuario ingresa la opción deseada y se actualiza el valor correspondiente en el objeto del cliente seleccionado.
    Si el cliente es de tipo natural, se pueden modificar el nombre, la cédula, el correo electrónico, la dirección y el teléfono.
    Si el cliente es de tipo jurídico, se pueden modificar la razón social, el RIF, el correo electrónico, la dirección y el teléfono.
    Los cambios se aplican directamente al objeto del cliente en la lista de clientes.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

"""
        for i,client in enumerate(self.clients):
            if isinstance(client, Client_natural):
                print(f"{i+1}- {client.name}")
            else:
                print(f"{i+1}- {client.social}")

        option = input("\nIngrese el numero del cliente que desea modificar: ")
        while not option.isnumeric():
            option = input("Error! Ingrese un valor valido: ")
        if isinstance(client, Client_natural):
            option_1 = input('\n1. Nombre \n2. ID \n3. Email \n4. Direccion \n5. Telefono: \nOpcion: ')
            if option_1 == "1":
                self.clients[int(option)-1].name = input("\nIngrese el nuevo nombre: ")
            elif option_1 == "2":
                while True: 
                    try:
                        self.clients[int(option)-1].id = float(input("\nIngrese la nueva cedula: "))
                        break
                    except:
                        print("Error! Ingrese un valor valido")
            elif option_1 == "3":
                self.clients[int(option)-1].email = input("\nIngrese el nuevo correo electronico: ")
            elif option_1 == "4":
                self.clients[int(option)-1].address = input("\nIngrese la nueva direccion: ")
            elif option_1 == "5":
                self.clients[int(option)-1].phone = input("\nIngrese el nuevo numero telefonico: ")
        else: 
            option_1 = input('\n1. Razon social \n2. RIF \n3. Email \n4. Direccion \n5. Telefono: \nOpcion: ')
            if option_1 == "1":
                self.clients[int(option)-1].name = input("\nIngrese el nuevo nombre: ")
            elif option_1 == "2":
                while True: 
                    try:
                        self.clients[int(option)-1].id = float(input("\nIngrese el nuevo RIF+: "))
                        break
                    except:
                        print("Error! Ingrese un valor valido")
            elif option_1 == "3":
                self.clients[int(option)-1].email = input("\nIngrese el nuevo correo electronico: ")
            elif option_1 == "4":
                self.clients[int(option)-1].address = input("\nIngrese la nueva direccion: ")
            elif option_1 == "5":
                self.clients[int(option)-1].phone = input("\nIngrese el nuevo numero telefonico: ")
#Borrar
    def erase_clients(self):
        for i,client in enumerate(self.clients):
            if isinstance(client, Client_natural):
                print(f"{i+1}- {client.name}")
            else:
                print(f"{i+1}- {client.social}")
        option = input("\nIngrese el numero del cliente que desea eliminar: ")
        while not option.isnumeric() or not int(option) in range(1, len(self.clients)+1):
            option = input("Error! Ingrese un valor valido: ")
        self.clients.pop(int(option)-1)
        print("Cliente eliminado exitosamente")
#Filtros 
    def filter_email(self):
        """
    Elimina un cliente existente del sistema.

    Muestra la lista de clientes disponibles y solicita al usuario ingresar el número del cliente que desea eliminar.
    El usuario debe ingresar un número válido correspondiente a un cliente existente en la lista.
    Una vez seleccionado el cliente, se elimina de la lista de clientes utilizando el método `pop()`.
    Se muestra un mensaje indicando que el cliente ha sido eliminado exitosamente.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        option = input("\nIngrese el correo de la persona o entidad: ")
        for client in self.clients:
            if option.lower() in client.email.lower():
                print(client.show_client())

    def filter_id(self):
        """
    Filtra y muestra los clientes que coinciden con un número de cédula o RIF específico.

    Solicita al usuario ingresar un número de cédula o RIF.
    Recorre la lista de clientes y compara el número ingresado con el número de cédula o RIF de cada cliente.
    Si hay coincidencia, se muestra la información del cliente utilizando el método `show_client()`.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        option = input("\nIngrese la cedula o rif: ")
        for client in self.clients:
            if isinstance(client, Client_natural):
                if option.lower() in client.id.lower():
                    print(client.show_client())
            else:
                if option.lower() in client.rif.lower():
                    print(client.show_client())

#Menu de clientes
    def menu_clients(self):
          while True: 
            option = input('''
--- Menu de clientes ---

1. Registrar
2. Modificar
3. Eliminar
4. Buscar
5. Regresar

''')
            while not option in ["1", "2", "3", "4", "5"]:
                option = input("Error! Ingrese un valor valido: ")
            
            if option == "1":
                self.register_clients()

            elif option == "2":
                self.modify_clients()

            elif option == "3":
                self.erase_clients()

            elif option == "4":
                while True: 
                    opcion_1 = input('''
--- Menu de busqueda de clientes ---

1. Por correo
2. Por ID
3. Regresar

''')
                    if opcion_1 == "1":
                        self.filter_email()
                    elif opcion_1 == "2":
                        self.filter_id()
                    else:
                        break
            else: 
                break