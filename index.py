class User:
    def __init__(self, name):
        self.name = name
        self.cash = 0
    def deposit(self, deposit):
        self.cash += deposit
    def withdraw(self, withdraw):
        self.cash -= withdraw
    def balance(self):
        print(f"{self.name}, Balance of: {self.cash}")


samuel = User("Samuel")
jack = User("Jack")
alice = User("Alice")

samuel.deposit(3000)
samuel.deposit(500)
samuel.deposit(10000)
samuel.withdraw(3000)
samuel.balance()
jack.deposit(2000)
jack.deposit(2000)
jack.withdraw(1000)
jack.withdraw(1000)
jack.balance()
alice.deposit(40000)
alice.withdraw(1000)
alice.withdraw(1000)
alice.withdraw(1000)
alice.balance()
