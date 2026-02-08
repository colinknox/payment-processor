class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Processing ${self.amount} cash payment")
        return True
    

    
payment = CashPayment(100)

print(payment.amount)
print(payment.process_payment())