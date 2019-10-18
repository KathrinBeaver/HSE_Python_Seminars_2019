import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)  # sqrt(x*x + y*y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __hash__(self):
        return hash(str(self.x + self.y))

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return False
        return hash(self) == hash(other)

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

vectors = set()
v1 = Vector2D(1, 2)
vectors.add(v1)
v2 = Vector2D(3, 4)
vectors.add(v2)
v3 = Vector2D(1, 2)
v3 += Vector2D(9, 9)
vectors.add(v3)
v4 = v3 - Vector2D(2, 2)
vectors.add(v4)

print(vectors)
# print(sorted(vectors))

v5 = Vector2D(2, 1)
vectors.add(v5)

print(vectors)


