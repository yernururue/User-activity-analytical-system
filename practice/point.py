class Point:
    def __init__(self, point1, point2):
        if point1 is None and point2 is None:
            self.point1 = 0
            self.point2 = 0
        else:
            self.point1 = point1
            self.point2 = point2
        
    def distance_from_origin(self):
        distance = ((self.point2)**2 + (self.point1)**2)**0.5
        return distance

    def distance(self, x2, y2):
        distance = ((y2-self.point2)**2 + (x2-self.point1)**2)**0.5
        print(f"distance between x1,y2 to x2,y2: {distance}")
        return distance

    def translate(self, dx, dy):
        self.point1 += dx
        self.point2 += dy
        return point1, point2

    def prr(self):
        print(f"x: {self.point1} y: {self.point2}")    
        print(f"distance from origin:{self.distance_from_origin()} ")


point = Point(5,5)
point.prr()


class Shape:
    def __init__(self, points):
        self.points = points
    def add_point(self, point):
        points.append(point)