from Client import Client

class Client_juridico(Client):
    
    def __init__(self, param_social: str, param_rif: int, param_email: str, param_address: str, param_phone: str):
        self.social = param_social
        self.rif = param_rif
        super().__init__(param_email, param_address, param_phone)

    def show_client(self):
        return f'''
---{self.social}---      
RIF: {self.rif}
Email: {self.email}  
Direccion: {self.address}    
Telefono: {self.phone}
'''