from Client import Client

class Client_natural(Client):
    
    def __init__(self, param_name: str, param_id: int, param_email: str, param_address: str, param_phone: str):
        self.name = param_name
        self.id = param_id
        super().__init__(param_email, param_address, param_phone)

    def show_client(self):
        return f'''
---{self.name}---      
ID: {self.id}
Email: {self.email}  
Direccion: {self.address}    
Telefono: {self.phone}
'''