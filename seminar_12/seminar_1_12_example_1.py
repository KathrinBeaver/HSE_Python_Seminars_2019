class A:
    def __init__(self, newB = 0):
        self.b = newB

    def __str__(self):
        return "str: " + str(self.b)

    def __repr__(self):
        return "repr: " + str(self.b)


print(A())
print(A(3))
