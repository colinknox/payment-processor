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

    def process_payment(self):
        print(f"Processing ${self.amount} credit card payment (card ending in {self.card_number})")
        return True

class CryptoPayment:
    def __init__(self, amount, wallet_address):
        self.amount = amount
        self.wallet_address = wallet_address

    def process_payment(self):
        print(f"Processing ${self.amount} crypto payment to wallet {self.wallet_address}")
        return True

def process_all_payments(payment_list):
    total_amount = 0
    
    for current_payment in payment_list:
        current_payment.process_payment()
        total_amount += current_payment.amount

    return total_amount
