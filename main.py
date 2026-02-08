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
        print(f"Processing ${self.amount} credit card payment (card ending in {self.card_number})")
        return True

class CryptoPayment:
    def __init__(self, amount, wallet_address):
        self.amount = amount
        self.wallet_address = wallet_address

    def process_payment(self):
        print(f"Processing ${self.amount} crypto payment to wallet {self.wallet_address}")
        return True

payment = CashPayment(100)
credit_card_payment = CreditCardPayment(500, 1324)
crypto_payment = CryptoPayment(250, 51235)

print(crypto_payment.amount)
print(crypto_payment.wallet_address)
print(crypto_payment.process_payment())
