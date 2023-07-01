from Product import Product


class Product_management:

    def __init__(self):
        self.products = []

    def register_products(self, list_products):
        """
    Registra una lista de productos y devuelve una lista de objetos de la clase Product.

    Args:
        self: El objeto de la clase que invoca el método.
        list_products (list): Una lista de diccionarios que contienen la información de los productos. Cada diccionario debe tener las siguientes claves:
            - "name" (str): El nombre del producto.
            - "description" (str): La descripción del producto.
            - "price" (float): El precio del producto.
            - "category" (str): La categoría del producto.

    Returns:
        list: Una lista de objetos de la clase Product creados a partir de los diccionarios de productos proporcionados.

    """
        new_products = []
        for producto in list_products:
            new_products.append(Product(producto["name"], producto["description"], producto["price"], producto["category"]))
        return new_products
    
    def filter_category(self):
        """
    Filtra y muestra los productos de una categoría específica.

    Muestra una lista de categorías disponibles y solicita al usuario que ingrese el número correspondiente a la categoría que desea consultar. Luego, muestra los productos pertenecientes a la categoría seleccionada.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        aux = []
        for producto in self.products:
            if not producto.category in aux:
                aux.append(producto.category)
        for i,category in enumerate(aux):
            print(f"{i+1}- {category}")
        option = input("Ingrese el numero de la categoria que desea consultar: ")
        while not option.isnumeric() or not int(option) in range(1, len(aux)+1):
            option = input("Error! Ingrese un valor valido: ")
        for producto in self.products:
            if producto.category == aux[int(option)-1]:
                print(producto.show_product())

    def filter_price(self):
        """
    Filtra y muestra los productos que están dentro de un rango de precios especificado por el usuario.

    Solicita al usuario que ingrese un precio mínimo y un precio máximo. Luego, muestra los productos cuyos precios se encuentran dentro del rango especificado.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        while True:
            try: 
                inf = float(input("Ingrese un precio minimo: "))
                sup = float(input("Ingrese un precio maximo: "))
                if inf >= sup: 
                    raise Exception
                break
            except:
                print("Error! Ingrese valores validos ")
        for producto in self.products:
            if inf<=  producto.price <= sup:
                print(producto.show_product())

    def filter_name(self):
        """
    Filtra y muestra los productos que coinciden parcialmente con un nombre especificado por el usuario.

    Solicita al usuario que ingrese el nombre de un producto y luego muestra los productos cuyos nombres coinciden parcialmente con el nombre especificado (ignorando mayúsculas y minúsculas).

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        option = input("Ingrese el nombre del producto: ")
        for producto in self.products:
            if option.lower() in producto.name.lower():
                print(producto.show_product())

    def filter_availability(self):
        """
    Filtra y muestra los productos disponibles o los productos agotados según la elección del usuario.

    Solicita al usuario que elija si desea ver los productos disponibles o los productos agotados. Luego, muestra los productos correspondientes según la elección realizada.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        option = input("Desea ver los productos disponibles o los que estan agotados? ('1' para ver los disponibles, '2' para ver los agotados): ")
        while not option in ["1", "2"]:
                option = input("Error! Ingrese un valor valido: ")
        if option == "1":
            for producto in self.products:
                if producto.inventory > 0:
                    print(producto.show_product())
        else:
            for producto in self.products:
                if producto.inventory == 0:
                    print(producto.show_product())

    def erase_products(self):
        """
    Elimina un producto de la lista de productos.

    Muestra una lista numerada de los productos disponibles y solicita al usuario que ingrese el número correspondiente al producto que desea eliminar. Luego, elimina el producto seleccionado de la lista.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        for i,product in enumerate(self.products):
            print(f"{i+1}- {product.name}")
        option = input("Ingrese el numero del producto que desea eliminar: ")
        while not option.isnumeric() or not int(option) in range(1, len(self.products)+1):
            option = input("Error! Ingrese un valor valido: ")
        self.products.pop(int(option)-1)
        print("Producto eliminado exitosamente")

    def modify_products(self):
        """
    Modifica los atributos de un producto específico.

    Muestra una lista numerada de los productos disponibles y solicita al usuario que ingrese el número correspondiente al producto que desea modificar. Luego, ofrece opciones para modificar diferentes atributos del producto seleccionado, como nombre, descripción, precio y categoría.

    Args:
        self: El objeto de la clase que invoca el método.

    Returns:
        None

    """
        for i,product in enumerate(self.products):
            print(f"{i+1}- {product.name}")
        option = input("Ingrese el numero del producto que desea modificar: ")
        while not option.isnumeric() or not int(option) in range(1, len(self.products)+1):
            option = input("Error! Ingrese un valor valido: ")
        option_1 = input('\n1. Nombre \n2. Descripcion \n3. Precio \n4. Categoria')
        if option_1 == "1":
            self.products[int(option)-1].name = input("Ingrese el nuevo nombre del producto: ")
        elif option_1 == "2":
            self.products[int(option)-1].description = input("Ingrese la nueva descripcion: ")
        elif option_1 == "3":
            while True: 
                try:
                    self.products[int(option)-1].price = float(input("Ingrese el nuevo precio del producto: "))
                    break
                except:
                    print("Error! Ingrese un valor valido")
        else:
            self.products[int(option)-1].category = input("Ingrese la nueva categoria del producto: ").capitalize
        

    def menu_products(self, products):
        self.products = products
        while True: 
            option = input('''
--- Menu de productos ---

1. Buscar
2. Modificar
3. Eliminar
4. Regresar

''')
            while not option in ["1", "2", "3","4"]:
                option = input("Error! Ingrese un valor valido: ")
            
            if option == "1":
                while True: 
                    option_1 = input('''
--- Menu de busqueda ---

1. Categoria
2. Precio
3. Nombre
4. Disponibilidad
5. Regresar al menu de productos 

''')
                    while not option_1 in ["1", "2", "3", "4","5"]:
                        option_1 = input("Error! Ingrese un valor valido: ")

                    if option_1 == "1":
                        self.filter_category()
                    elif option_1 == "2":
                        self.filter_price()
                    elif option_1 == "3":
                        self.filter_name()
                    elif option_1 == "4":
                        self.filter_availability()
                    elif option_1 == "5":
                        break
                    
            elif option == "2":
                self.modify_products()
            elif option == "3":
                self.erase_products()
            else:
                break