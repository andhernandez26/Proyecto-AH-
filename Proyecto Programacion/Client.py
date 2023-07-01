class Client:
    
    def __init__(self, param_email: str, param_address: str, param_phone: str):
        self.email = param_email
        self.address = param_address
        self.phone = param_phone
        self.total_purchases = 0

    def show_client(self):
        return f'''
Email: {self.email}  
Direccion: {self.address}    
Telefono: {self.phone}
'''