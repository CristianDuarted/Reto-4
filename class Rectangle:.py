import math

class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    def get_x(self) -> int:
        return self._x
    
    def set_x(self, new_x:int):
        self._x = new_x

    def get_y(self) -> int:
        return self._y
    
    def set_y(self, new_y:int):
        self._x = new_y
    
    def __str__(self):
        return f"({self._x}, {self._y})"
    
    def __repr__(self):
        return f"Point({self._x}, {self._y})"

class Line:
    def __init__ (self, start: Point, end: Point):
        self._start = start
        self._end = end
    
    def get_sart(self) -> int:
        return self._start
        
    def set_start(self, new_start:int):
        self._start = new_start

    def get_end(self) -> int:
        return self._end
    
    def set_end(self, new_end:int):
        self._end = new_end


    
    def compute_length(self):
        lenght = math.sqrt((self._start._x - self._end._x ) ** 2 + (self._start._y - self._end._y) ** 2)
        return lenght
    
    def compute_slope(self):
       if self._end._x != self._start._x:
            slope = (self._start._y - self._end._y) / (self._start._x - self._end._x)
            angle = math.degrees(math.atan(slope))
            return angle
       else:
            return 90
    
    def compute_horizontal_cross(self) -> bool:
        if (self._end._y <= 0 and self._start._y >= 0) or (self._end._y >= 0 and self._start._y <= 0):
            return True
        else:
            return False

    def compute_vertical_cross(self) -> bool:  
        if (self._end._x <= 0 and self._start._x >= 0) or (self._end._x >= 0 and self._start._x <= 0):
            return True
        else:
            return False

class Shape:
    def __init__(self, is_regular: bool, vertices: list[Point], edges:list[Line], inner_angles: list[float]):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
    
    def get_is_regular(self):
        return self._is_regular
    
    def set_is_regular(self, new_is_regular):
        self._new_is_regular = new_is_regular

    def get_vertices(self):
        return self._vertices
    
    def set_vertices(self, new_vertices):
        self._vertices = new_vertices
    
    def get_edges(self):
        return self._edges
    
    def set_edges(self, new_edges):
        self._new_edges = new_edges

    def get_inner_angles(self):
        return self._inner_angles
    
    def set_inner_angles(self, new_inner_angles):
        self._inner_angles = new_inner_angles

    def compute_area(self):
        pass

    def compute_perimeter(self)->float:
        perimeter = 0
        for edge in self._edges:
            perimeter += edge.compute_length()
        return perimeter    

    def compute_inner_angles(self):
        pass    
        



class Rectangle(Shape):
    def __init__(self, **kwargs):
        
        if "width" in kwargs and "height" in kwargs and "center" in kwargs:
            self._width = kwargs["width"] 
            self._height = kwargs["height"]
            self._center = kwargs["center"]
         
        elif "point1" in kwargs and "point2" in kwargs:
            self.point1 = kwargs["point1"]
            self.point2 = kwargs["point2"]
            self._width = abs(self.point2._x - self.point1._x)
            self._height = abs(self.point2._y - self.point1._y)
            center_x = (self.point1._x + self.point2._x) / 2
            center_y = (self.point1._y + self.point2._y) / 2
            self._center = Point(center_x, center_y)
        elif "width" in kwargs and "height" in kwargs and "bottom_left" in kwargs:
            self._width = kwargs["width"] 
            self._height = kwargs["height"]
            self.bottom_left = kwargs["bottom_left"]
            center_x = (self.bottom_left._x + self.width /2)
            center_y = (self.bottom_left._y + self.height /2)
            self._center = Point(center_x, center_y)

        elif "line1" in kwargs and "line2" in kwargs and "line3" in kwargs and "line4" in kwargs:
            self.line1 = kwargs ["line1"]
            self.line2 = kwargs ["line2"]
            self.line3 = kwargs ["line3"]
            self.line4 = kwargs ["line4"]
            if (self.line1.compute_length() == self.line2.compute_length()):
                if (self.line4.compute_length() == self.line3.compute_length()):
                    self._width = self.line1.compute_length()
                    self._height = self.line3.compute_length()
                    center_x = ((self.line1._start._x + self.line2._end._x) /2)
                    center_y = ((self.line1._end._y+ self.line2._start._y) /2)
                    self._center = Point(center_x, center_y)
                else:
                    return ValueError("Parámetros inválidos")
            elif (self.line1.compute_length() == self.line3.compute_length()):
                 if (self.line2.compute_length() == self.line4.compute_length()):
                    self._width = self.line1.compute_length()
                    self._height = self.line4.compute_length()
                    center_x = ((self.line1._end._x + self.line3._start._x) /2)
                    center_y = ((self.line1._start._y + self.line3._end._y) /2)
                    self._center = Point(center_x, center_y)
            elif (self.line1.compute_length() == self.line4.compute_length()):
                if (self.line2.compute_length() == self.line3.compute_length()):
                    self._width = self.line1.compute_length()
                    self._height = self.line3.compute_length()
                    center_x = ((self.line1._start._x + self.line4._start._x) /2)
                    center_y = ((self.line2._end._y + self.line4._end._y) /2)
                    self._center = Point(center_x, center_y)
            else:
                ValueError("Parámetros inválidos")
        
        else:
             raise ValueError("Parámetros inválidos")
        half_width = self._width / 2
        half_height = self._height / 2

        def get_width(self):
            return self._width 

        def set_width(self, new_width):
            self._width = new_width

        def get_height(self):
            return self._height
            
        def set_height(self, new_height):
            self._height = new_height

        def get_center(self):
            return self._center
            
        def set_center(self, new_center):
            self._center = new_center 

        p1 = Point(self._center._x - half_width, self._center._y - half_height)
        p2 = Point(self._center._x + half_width, self._center._y - half_height)
        p3 = Point(self._center._x + half_width, self._center._y + half_height)
        p4 = Point(self._center._x - half_width, self._center._y + half_height)

        vertices = [p1, p2, p3, p4] 

        edges = [
        Line(p1, p2),
        Line(p2, p3),
        Line(p3, p4),
        Line(p4, p1)
        ]

        inner_angles = [90, 90, 90, 90]

        is_regular = self._width == self._height  

        super().__init__(is_regular, vertices, edges, inner_angles)


    def compute_area(self) -> float:
        return self._width * self._height


    
    def __str__(self):
        return f"Rectangle(width = {self._width}, height = {self._height}, center = ({self._center._x}, {self._center._y}))"

class Square(Rectangle):
    def __init__(self, side, center):
        super().__init__(width=side, height=side, center=center)



class Triangle(Shape):
    def __init__(self,**kwargs):       
        p1 = kwargs["vertice1"]
        p2 = kwargs["vertice2"]
        p3 = kwargs["vertice3"]
        vertices = [p1,p2,p3]
        self.line1= Line(p1,p2)
        self.line2= Line(p2,p3)
        self.line3= Line(p3,p1)
        edges = [self.line1,self.line2,self.line3]
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()
        if (round(a,5) == round(b,5) == round(c,5)):
            is_regular = True
        else:
          is_regular = False
        inner_angles = []    
        super().__init__(is_regular, vertices, edges, inner_angles)
    def compute_area(self) -> float:
        #formula de heron
        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()

        semiperimetro = (a + b + c) / 2
        area = math.sqrt(semiperimetro*
                         (semiperimetro - a)*
                         (semiperimetro - b)*
                         (semiperimetro - c))
        return area

class Equilateral(Triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()

        if not (round(a, 5) == round(b, 5) == round(c, 5)):
            raise ValueError("No es un triángulo equilátero")
        
        
class Isosceles(Triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()

        if not (a == b or b == c or a == c):
            raise ValueError("No es un triángulo isósceles")

class Scalene(Triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()

        if (a == b or b == c or a == c):
            raise ValueError("No es un triángulo escaleno")
        
class TriRectangle(Triangle):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        a = self.line1.compute_length()
        b = self.line2.compute_length()
        c = self.line3.compute_length()

        lados = sorted([a, b, c])

        if not (lados[0]**2 + lados[1]**2 == lados[2]**2):
            raise ValueError("No es un triángulo rectángulo")


print("=== RECTANGLE ===")
r = Rectangle(width=10, height=5, center=Point(0, 0))

print(f"Área rectángulo: {r.compute_area()}")
print(f"Perímetro rectángulo: {r.compute_perimeter()}")
print(f"Vértices rectángulo: {r.get_vertices()}")


print("\n=== SQUARE ===")
s = Rectangle(width=4, height=4, center=Point(0, 0))

print(f"Área cuadrado: {s.compute_area()}")
print(f"Perímetro cuadrado: {s.compute_perimeter()}")
print(f"¿Es regular?: {s.get_is_regular()}")


print("\n=== TRIANGLE 3-4-5 ===")
t = Triangle(
    vertice1=Point(0, 0),
    vertice2=Point(4, 0),
    vertice3=Point(0, 3)
)

print(f"Área triángulo: {t.compute_area()}")
print(f"Perímetro triángulo: {t.compute_perimeter()}")
print(f"Vértices triángulo: {t.get_vertices()}")


print("\n=== TRI-RECTANGLE ===")
tr = TriRectangle(
    vertice1=Point(0, 0),
    vertice2=Point(4, 0),
    vertice3=Point(0, 3)
)

print(f"Área triángulo rectángulo: {tr.compute_area()}")
print(f"Perímetro triángulo rectángulo: {tr.compute_perimeter()}")


print("\n=== ISOSCELES ===")
iso = Isosceles(
    vertice1=Point(0, 0),
    vertice2=Point(4, 0),
    vertice3=Point(2, 3)
)

print(f"Área isósceles: {iso.compute_area()}")
print(f"Perímetro isósceles: {iso.compute_perimeter()}")


print("\n=== SCALENE ===")
sca = Scalene(
    vertice1=Point(0, 0),
    vertice2=Point(4, 0),
    vertice3=Point(1, 3)
)

print(f"Área escaleno: {sca.compute_area()}")
print(f"Perímetro escaleno: {sca.compute_perimeter()}")


print("\n=== EQUILATERAL ===")
eq = Equilateral(
    vertice1=Point(0, 0),
    vertice2=Point(2, 0),
    vertice3=Point(1, math.sqrt(3))
)

print(f"Área equilátero: {eq.compute_area()}")
print(f"Perímetro equilátero: {eq.compute_perimeter()}")
print(f"¿Es regular?: {eq.get_is_regular()}")