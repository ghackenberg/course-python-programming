class Vehicle:
    def __eq__(self, other):
        return True
    
v1 = Vehicle()
v2 = Vehicle()

print(v1 == v2)
print(v1.__eq__(v2))