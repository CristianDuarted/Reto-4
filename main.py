class MenuItem:
    def __init__ (self, name:str, price:float):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price  

class Drink(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super ().__init__(name, price)
        self.size = size

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)

class Order:
    def __init__(self):
        self.items: list[MenuItem] = []

    def add_item(self, item: MenuItem) -> None:
        self.items.append(item)

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item.calculate_price()
        return total
    
aperitvo1 = Appetizer("Nachos" , 6)
aperitvo2 = Appetizer("Alitas", 9)

principal1 = MainCourse("Pizza", 10)
principal2 = MainCourse("Hamburguesa", 9)
principal3 = MainCourse("Pasta", 11)

bebida = Drink("Coca-Cola", 5, "grande")
bebida2 = Drink("Agua", 3, "pequeña")
bebida3 = Drink("Jugo", 6, "mediano")

postre1 = MenuItem("Helado", 3)
postre2 = MenuItem("Torta", 4)

orden1 =Order ()
orden1.add_item(aperitvo1)
orden1.add_item(principal1)
orden1.add_item(bebida2)
orden1.add_item(postre1)

print(orden1.calculate_total())