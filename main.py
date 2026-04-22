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
        
        if total > 20:
            discount = total * 0.10
            total -= discount 

        if total > 30:
            discount = total * 0.20
            total -= discount     
        return total
    def __str__ (self):
        return f"Item1: {self.items}"
    
    def show_order(self):
      print ("TU ORDEN:")
      print("-------------------")
    
      for item in self.items:

        if isinstance(item, Drink):
            print(f"{item.name} ({item.size}) - ${item.price}")
        else:
            print(f"{item.name} - ${item.price}")
    
        print("-------------------")
        print(f"TOTAL: ${self.calculate_total()}")
    
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

print("===== PRUEBA DEL SISTEMA =====")

order = Order()

# Agregar items
order.add_item(Appetizer("Nachos", 6))
order.add_item(Appetizer("Alitas", 9))
order.add_item(MainCourse("Pizza", 10))
order.add_item(Drink("Coca-Cola", 3, "Grande"))

# Mostrar orden
order.show_order()

print("\n===== PRUEBAS INDIVIDUALES =====")

# Test sin descuento
order1 = Order()
order1.add_item(MainCourse("Pizza", 10))
order1.add_item(Drink("Agua", 2, "Pequeña"))
print("Total esperado 12:", order1.calculate_total())

# Test descuento 10%
order2 = Order()
order2.add_item(Appetizer("Nachos", 6))
order2.add_item(Appetizer("Alitas", 9))
order2.add_item(MainCourse("Pizza", 10))
print("Total esperado 22.5:", order2.calculate_total())

# Test descuento 20%
order3 = Order()
order3.add_item(MainCourse("Pizza", 10))
order3.add_item(MainCourse("Hamburguesa", 12))
order3.add_item(MainCourse("Pasta", 10))
print("Total esperado 25.6:", order3.calculate_total())

print("\n===== TEST DE DIFERENTES TIPOS =====")

drink = Drink("Jugo", 4, "Mediano")
app = Appetizer("Papas", 5)
main = MainCourse("Lasagna", 11)

print(drink.name, drink.price, drink.size)
print(app.name, app.price)
print(main.name, main.price)