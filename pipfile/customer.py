class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be 1-15 characters")
        self._name = value
        
    def orders(self):
        return self._orders
        
    def coffees(self):
        return list({order.coffee for order in self._orders})
        
    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        return order


alice = Customer("Alice")
bob = Customer("Bob")

espresso = Coffee("Espresso")
latte = Coffee("Latte")

order1 = Order(alice, espresso, 3.5)
order2 = Order(bob, espresso, 4.0)
order3 = Order(alice, latte, 5.0)

print(alice.orders())
print(espresso.customers())
print(latte.num_orders())