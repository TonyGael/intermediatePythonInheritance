class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "X: {}, Y: {}".format(self.x, self.y)


vector_1 = Vector(2, 5)
vector_2 = Vector(6, 3)

print(vector_1)
print(vector_2)

vector_3 = vector_1 + vector_2
print(vector_3)

vector_3 = vector_1 - vector_2
print(vector_3)
