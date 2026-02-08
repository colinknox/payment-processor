class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def process_payment(self):
        print(f"Processing ${self.amount} cash payment")
        return True
    
class CreditCardPayment:
    def __init__(self, amount, card_number):
        self.amount = amount
        self.card_number = card_number

    def payment_process(self):
        print(f"Processing {self.amount} credit card payment (card ending in {self.card_number})")
        return True



payment = CashPayment(100)
credit_card_payment = CreditCardPayment(500, 1324)

print(f"DEBUG: Credit card payment amount = {credit_card_payment.amount}")
print(f"DEBUG: Credit card number = {credit_card_payment.card_number}")