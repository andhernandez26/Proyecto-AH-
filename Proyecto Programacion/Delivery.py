from Order import Order

class Delivery: 

    def __init__(self, param_client: str, param_date, param_service: str, param_moto: dict):
        self.client = param_client
        self.date = param_date
        self.service = param_service
        self.moto = param_moto

    def show_moto(self):
        return f''''
Nombre: {self.moto["name"]}
ID: {self.moto["ID"]}
Telefono: {self.moto["Telefono"]}
        '''
    
    def show_delivery(self):
        if self.service == "Delivery":
            return f"""
--- Envio ---

Servicio: {self.service}
Fecha: {self.date}
Motorizado: {self.show_moto()}"""
        else:
            return f"""
--- Envio --- 

Servicio: {self.service} 
Fecha: {self.date}"""