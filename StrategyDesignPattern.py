from abc import ABC, abstractmethod

# Step 1: Define the Strategy Interface (Abstract Base Class)
class PaymentStrategy(ABC):
    """The Strategy interface declares operations common to all supported versions of some algorithm."""
    @abstractmethod
    def pay(self, amount: float):
        pass

# Step 2: Implement Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    """Implements the algorithm for credit card payment."""
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        print(f"Paid {amount:.2f} using Credit Card ending with {self.card_number[-4:]}")

class PayPalPayment(PaymentStrategy):
    """Implements the algorithm for PayPal payment."""
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float):
        print(f"Paid {amount:.2f} using PayPal account {self.email}")

# Step 3: Create the Context Class
class PaymentContext:
    """The Context stores a reference to one of the concrete strategies and communicates with it."""
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        """Allows replacing the strategy object at runtime."""
        self._strategy = strategy

    def process_payment(self, amount: float):
        """Delegates the payment behavior to the selected strategy."""
        print(f"Processing payment...")
        self._strategy.pay(amount)

# Step 4: Use the Strategy Pattern (Client Code)
if __name__ == "__main__":
    # The client creates concrete strategy objects and passes them to the context.

    # Option 1: Pay with Credit Card
    credit_card_option = CreditCardPayment("1234567890123456")
    context = PaymentContext(credit_card_option)
    context.process_payment(100.00)

    print("-" * 20)

    # Option 2: Switch strategy at runtime to PayPal
    paypal_option = PayPalPayment("user@example.com")
    context.set_strategy(paypal_option)
    context.process_payment(50.50)

    # Adding a new payment method (e.g., Bitcoin) is simple:
    # 1. Create a new class implementing PaymentStrategy.
    # 2. Pass an instance of the new class to the context.
    # No modifications to the PaymentContext class are needed.
