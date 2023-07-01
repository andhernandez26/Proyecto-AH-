import random

class Product:

    def __init__(self, param_name: str, param_description: str, param_price: int, param_category: str):
        self.name = param_name
        self.description = param_description
        self.price = param_price
        self.category = param_category
        self.inventory = random.randint(1, 100)
        self.times_sold = 0
        self.times_sent = 0 
        
    def show_product(self):
        return f'''
---{self.name}---       
Descripcion: {self.description}
Precio: ${self.price}
Categoria: {self.category}  
Inventario: {self.inventory}    
'''
