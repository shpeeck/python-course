import math

class Point2D:
    
    _count = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point2D._count += 1
        
    @property
    def count(self):
        return self._count

    def distance(self, xy):
        return math.sqrt(((self.x - xy.x) ** 2) + ((self.y - xy.y) ** 2))
    
class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        
    def distance(self, xy):
        return math.sqrt(((self.x - xy.x) ** 2) + ((self.y - xy.y) ** 2) + ((self.z - xy.z) ** 2))
    
    
p1 = Point2D(10, 10)
p2 = Point2D(20, 20)

print(p1.distance(p2))
print(p1.count)

p3 = Point3D(10, 10, 10)
p4 = Point3D(20, 20, 20)
print(p3.distance(p4))
print(p1.count)