from Client import Client

class Payment:

    def __init__(self, param_client: str, param_amount: float, param_coin: str, param_payment_type: str, param_date: str):
        self.client = param_client
        self.amount = param_amount
        self.coin = param_coin
        self.payment_type = param_payment_type
        self.date = param_date
   
    def show_payment(self):
        return f'''
---{self.client}---       
Monto: ${self.amount}
Moneda: {self.coin}
Tipo de pago: {self.payment_type}  
Fecha: {self.date}    
''' 