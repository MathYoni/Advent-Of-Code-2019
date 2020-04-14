class Moon:
    def __init__(self, position, velocity):
        self.pos = position
        self.vel = velocity

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
