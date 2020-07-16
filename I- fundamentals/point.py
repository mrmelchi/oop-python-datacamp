import math

class Point:
    def __init__(self, x= 0.0, y= 0.0):
        self.x = x
        self.y = y
    

    def distance_to_origin(self):
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))
    

    def reflect(self, axis):
        if axis == 'x':
            self.y = -1 * self.y
        elif axis == 'y':
            self.x = -1 * self.x
        else:
            print('Something went wrong')


if __name__ == "__main__":
    pt = Point(x=3.0)
    pt.reflect("y")
    print((pt.x, pt.y))
    pt.y = 4.0
    print(pt.distance_to_origin())