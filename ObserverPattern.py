from abc import ABC, abstractmethod

# --- 1. The Observer Interface ---
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        """Receive update from subject."""
        pass

# --- 2. The Subject (The thing being watched) ---
class Subject:
    def __init__(self):
        self._observers = [] # List of subscribers

    def attach(self, observer: Observer):
        """Add a subscriber."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        """Remove a subscriber."""
        self._observers.remove(observer)

    def notify(self, message: str):
        """Alert all subscribers."""
        for observer in self._observers:
            observer.update(message)

# --- 3. Concrete Observers (The listeners) ---
class EmailAlert(Observer):
    def update(self, message: str):
        print(f"Email Alert: Sending email with message -> {message}")

class SMSAlert(Observer):
    def update(self, message: str):
        print(f"SMS Alert: Sending text message -> {message}")

# --- 4. Execution ---
if __name__ == "__main__":
    # Initialize the Subject (e.g., a Stock Market Tracker)
    stock_market = Subject()

    # Initialize Observers
    user1_email = EmailAlert()
    user2_sms = SMSAlert()

    # Users subscribe to the market updates
    stock_market.attach(user1_email)
    stock_market.attach(user2_sms)

    print("--- First Update ---")
    stock_market.notify("Apple stock rose by 5%")

    # One user decides to unsubscribe
    stock_market.detach(user2_sms)

    print("\n--- Second Update ---")
    stock_market.notify("Tesla stock fell by 2%")

