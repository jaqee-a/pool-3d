class Vec3:

    @staticmethod
    def to_vec3(arr):
        return Vec3(arr[0], arr[1], arr[2])

    @staticmethod
    def div(vec, num):
        return Vec3(vec.x / num, vec.y / num, vec.z / num)

    @staticmethod
    def mul(vec, num):
        return Vec3(vec.x * num, vec.y * num, vec.z * num)


    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def normalize(self):
        self.n_div(self.magnitude())

    def normalized(self):
        mag = self.magnitude()

        if mag == 0: return Vec3(0, 0, 0)

        return Vec3.div(self, mag)

    def magnitude(self):
        return self.sqrmagnitude()**.5

    def sqrmagnitude(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def n_div(self, num):
        self.x /= num
        self.y /= num
        self.z /= num

    def n_mul(self, num):
        self.x *= num
        self.y *= num
        self.z *= num

    def values(self):
        return (self.x, self.y, self.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __div__(self, other):
        return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

class Vec2:

    @staticmethod
    def to_vec2(arr):
        return Vec2(arr[0], arr[1])

    @staticmethod
    def div(vec, num):
        return Vec2(vec.x / num, vec.y / num)

    @staticmethod
    def mul(vec, num):
        return Vec2(vec.x * num, vec.y * num)


    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x, self.y = x, y

    def normalize(self):
        self.n_div(self.magnitude())

    def normalized(self):
        mag = self.magnitude()

        if mag == 0: return Vec2(0, 0)

        return Vec2.div(self, mag)

    def magnitude(self):
        return self.sqrmagnitude()**.5

    def sqrmagnitude(self):
        return self.x ** 2 + self.y ** 2

    def n_div(self, num):
        self.x /= num
        self.y /= num

    def n_mul(self, num):
        self.x *= num
        self.y *= num

    def values(self):
        return (self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2(self.x * other.x, self.y * other.y)

    def __div__(self, other):
        return Vec2(self.x / other.x, self.y / other.y)

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"