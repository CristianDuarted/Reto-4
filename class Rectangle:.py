import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    
class Line:
    def __init__ (self, start: Point, end: Point):
        self.start = start
        self.end = end

    def compute_length(self):
        lenght = math.sqrt((self.start.x - self.end.x ) ** 2 + (self.start.y - self.end.y) ** 2)
        return lenght
    
    def compute_slope(self):
       if self.end.x != self.start.x:
            slope = (self.start.y - self.end.y) / (self.start.x - self.end.x)
            angle = math.degrees(math.atan(slope))
            return angle
       else:
            return 90
    
    def compute_horizontal_cross(self) -> bool:
        if (self.end.y <= 0 and self.start.y >= 0) or (self.end.y >= 0 and self.start.y <= 0):
            return True
        else:
            return False

    def compute_vertical_cross(self) -> bool:  
        if (self.end.x <= 0 and self.start.x >= 0) or (self.end.x >= 0 and self.start.x <= 0):
            return True
        else:
            return False
    
class Rectangle:
    def __init__(self, **kwargs):
        if "width" in kwargs and "height" in kwargs and "center" in kwargs:
            self.width = kwargs["width"] 
            self.height = kwargs["height"]
            self.center = kwargs["center"]        
        elif "point1" in kwargs and "point2" in kwargs:
            self.point1 = kwargs["point1"]
            self.point2 = kwargs["point2"]
            self.width = abs(self.point2.x - self.point1.x)
            self.height = abs(self.point2.y - self.point1.y)
            center_x = (self.point1.x + self.point2.x) / 2
            center_y = (self.point1.y + self.point2.y) / 2
            self.center = Point(center_x, center_y)
        elif "width" in kwargs and "height" in kwargs and "bottom_left" in kwargs:
            self.width = kwargs["width"] 
            self.height = kwargs["height"]
            self.bottom_left = kwargs["bottom_left"]
            center_x = (self.bottom_left.x + self.width /2)
            center_y = (self.bottom_left.y + self.height /2)
            self.center = Point(center_x, center_y)

        elif "line1" in kwargs and "line2" in kwargs and "line3" in kwargs and "line4" in kwargs:
            self.line1 = kwargs ["line1"]
            self.line2 = kwargs ["line2"]
            self.line3 = kwargs ["line3"]
            self.line4 = kwargs ["line4"]
            if (self.line1.compute_length() == self.line2.compute_length()):
                if (self.line4.compute_length() == self.line3.compute_length()):
                    self.width = self.line1.compute_length()
                    self.height = self.line3.compute_length()
                    center_x = ((self.line1.start.x + self.line2.end.x) /2)
                    center_y = ((self.line1.end.y+ self.line2.start.y) /2)
                    self.center = Point(center_x, center_y)
                else:
                    return ValueError("Parámetros inválidos")
            elif (self.line1.compute_length() == self.line3.compute_length()):
                 if (self.line2.compute_length() == self.line4.compute_length()):
                    self.width = self.line1.compute_length()
                    self.height = self.line4.compute_length()
                    center_x = ((self.line1.end.x + self.line3.start.x) /2)
                    center_y = ((self.line1.start.y + self.line3.end.y) /2)
                    self.center = Point(center_x, center_y)
            elif (self.line1.compute_length() == self.line4.compute_length()):
                if (self.line2.compute_length() == self.line3.compute_length()):
                    self.width = self.line1.compute_length()
                    self.height = self.line3.compute_length()
                    center_x = ((self.line1.start.x + self.line4.start.x) /2)
                    center_y = ((self.line2.end.y + self.line4.end.y) /2)
                    self.center = Point(center_x, center_y)
            else:
                ValueError("Parámetros inválidos")
       
        else:
             raise ValueError("Parámetros inválidos")
       

    def compute_area(self) -> str:
        return f"el area es: {self.width * self.height}"

    def compute_perimeter(self) -> str:
        return f"el perimetro es: {(self.width + self.height)*2}"
    
    def __str__(self):
        return f"Rectangle(width = {self.width}, height = {self.height}, center = ({self.center.x}, {self.center.y}))"
    


p1 = Point(2, 3)
p2 = Point(8, 7)

r1 = Rectangle(width=10, height=5, center=Point(0,0))
r2 = Rectangle(point1=p1, point2=p2)
r3 = Rectangle(width=10, height=5, bottom_left=p1)

print(r2.compute_perimeter())
print(r2)
print(r2.compute_area())




print("=== PRUEBAS POINT ===")
p1 = Point(2, 3)
p2 = Point(8, 7)

print(p1.x)
print(p1.y)
print(p2.x)
print(p2.y)


print("\n=== PRUEBAS LINE ===")
line1 = Line(Point(2, 3), Point(8, 7))
print(line1.compute_length())
print(line1.compute_slope())
print(line1.compute_horizontal_cross())
print(line1.compute_vertical_cross())

line2 = Line(Point(2, 3), Point(5, -2))
print(line2.compute_horizontal_cross())
print(line2.compute_vertical_cross())

line3 = Line(Point(-2, 3), Point(4, 5))
print(line3.compute_horizontal_cross())
print(line3.compute_vertical_cross())

line4 = Line(Point(2, 1), Point(2, 8))
print(line4.compute_length())
print(line4.compute_slope())
print(line4.compute_horizontal_cross())
print(line4.compute_vertical_cross())

line5 = Line(Point(1, 4), Point(7, 4))
print(line5.compute_length())
print(line5.compute_slope())
print(line5.compute_horizontal_cross())
print(line5.compute_vertical_cross())

line6 = Line(Point(-2, 0), Point(5, 0))
print(line6.compute_horizontal_cross())
print(line6.compute_vertical_cross())


print("\n=== PRUEBAS RECTANGLE ===")
r1 = Rectangle(width=10, height=5, center=Point(0, 0))
print(r1)
print(r1.compute_area())
print(r1.compute_perimeter())
print(r1.width)
print(r1.height)
print(r1.center.x)
print(r1.center.y)

r2 = Rectangle(point1=Point(2, 3), point2=Point(8, 7))
print(r2)
print(r2.compute_area())
print(r2.compute_perimeter())
print(r2.width)
print(r2.height)
print(r2.center.x)
print(r2.center.y)

r3 = Rectangle(width=10, height=5, bottom_left=Point(2, 3))
print(r3)
print(r3.compute_area())
print(r3.compute_perimeter())
print(r3.width)
print(r3.height)
print(r3.center.x)
print(r3.center.y)

a = Point(0, 0)
b = Point(6, 0)
c = Point(6, 4)
d = Point(0, 4)

l1 = Line(a, b)
l2 = Line(b, c)
l3 = Line(c, d)
l4 = Line(d, a)

r4 = Rectangle(line1=l1, line2=l2, line3=l3, line4=l4)
print(r4)
print(r4.compute_area())
print(r4.compute_perimeter())
print(r4.width)
print(r4.height)
print(r4.center.x)
print(r4.center.y)


print("\n=== PRUEBA ERROR ===")
try:
    malo = Rectangle(a=1, b=2)
    print(malo)
except Exception as e:
    print(type(e).__name__, e)