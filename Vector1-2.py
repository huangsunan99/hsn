import math
class Vector(object):
    def __init__(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def scale(self, fac):
        self.x *= fac
        self.y *= fac
        self.z *= fac

    def dot_product(self, v):
        assert isinstance(v, Vector)
        return self.x* v.x+self.y*v.y+self.z*v.z

    def cross_product(self, v):
        m = self.y*v.z-self.z*v.y
        n = self.z*v.x-self.x*v.z
        p = self.x*v.y-self.y*v.x
        return Vector(m, n, p)

if __name__ == '__main__':
    test_vector = Vector(1, 2, 3)
    print test_vector.length()
    print test_vector.scale(8)
    print test_vector.length()
    Vx = Vector(1.0, 0.0, 0.0)
    Vy = Vector(0.0, 1.0, 0.0)
    Vz = Vx.cross_product(Vy)
    pass