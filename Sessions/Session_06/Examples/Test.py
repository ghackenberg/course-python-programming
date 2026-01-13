# Value comparison (for primitive data types)!

x = 5
y = 5

print(x == y)

# Memory location comparison (for objects)!

class Customer:
    def __init__(self, name):
        self.name = name

customerA = Customer("Peter")
customerB = Customer("Peter")

print(customerA == customerB)

# Memory location stays the same, even if state changes!

print(customerB)
customerB.name = 5
print(customerB)