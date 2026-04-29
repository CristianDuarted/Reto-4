class MenuItem:
    def __init__ (self, name:str, price:float):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price

    def calculate_price(self):
        return self._price  
        


class Drink(MenuItem):
    def __init__(self, name: str, price: float, size: str):
        super ().__init__(name, price)
        self._size = size
   
    def get_size(self):
        return self._size

    def set_size(self, size):
   
        self._size = size


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
        has_main = False

        for item in self.items:
            if isinstance(item,MainCourse):
                has_main =True 

        for item in self.items:
            price = item.calculate_price()

            if has_main and isinstance(item, Drink):
                 price *= 0.9   # 10% descuento

            total += price  
        return total
    

    def __str__ (self):
        return f"Item1: {self.items}"
    
    def show_order(self):
      print ("TU ORDEN:")
      print("-------------------")
    
      for item in self.items:

        if isinstance(item, Drink):
            print(f"{item.get_name()} ({item.get_size()}) - ${item.get_price()}")
        else:
            print(f"{item.get_name()} - ${item.get_price()}")
    
        print("-------------------")
        print(f"TOTAL: ${self.calculate_total()}")

class Payment:
    def __init__(self, amount: float):
        self._amount = amount

    def pay(self):
        print(f"Pagando ${self._amount}")

class CardPayment(Payment):
    def pay(self):
        print(f"Pagando con tarjeta: ${self._amount}")

class CashPayment(Payment):
    def pay(self):
        print(f"Pagando en efectivo: ${self._amount}")

   
     
print("===== PRUEBA DEL SISTEMA =====")

order = Order()
order.add_item(Appetizer("Nachos", 6))
order.add_item(Appetizer("Alitas", 9))
order.add_item(MainCourse("Pizza", 10))
order.add_item(Drink("Coca-Cola", 3, "Grande"))

order.show_order()
print(f"Total esperado: 27.7")
print(f"Total obtenido: {order.calculate_total()}")


print("\n===== PRUEBA SIN PLATO PRINCIPAL =====")

order1 = Order()
order1.add_item(Appetizer("Nachos", 6))
order1.add_item(Drink("Agua", 2, "Pequeña"))

order1.show_order()
print(f"Total esperado: 8")
print(f"Total obtenido: {order1.calculate_total()}")


print("\n===== PRUEBA CON PLATO PRINCIPAL + BEBIDA =====")

order2 = Order()
order2.add_item(MainCourse("Pizza", 10))
order2.add_item(Drink("Agua", 2, "Pequeña"))

order2.show_order()
print(f"Total esperado: 11.8")
print(f"Total obtenido: {order2.calculate_total()}")


print("\n===== PRUEBA CON VARIOS PLATOS PRINCIPALES =====")

order3 = Order()
order3.add_item(MainCourse("Pizza", 10))
order3.add_item(MainCourse("Hamburguesa", 9))
order3.add_item(MainCourse("Pasta", 11))

order3.show_order()
print(f"Total esperado: 30")
print(f"Total obtenido: {order3.calculate_total()}")


print("\n===== PRUEBA CON VARIAS BEBIDAS Y PLATO PRINCIPAL =====")

order4 = Order()
order4.add_item(MainCourse("Hamburguesa", 9))
order4.add_item(Drink("Coca-Cola", 5, "Grande"))
order4.add_item(Drink("Jugo", 6, "Mediano"))
order4.add_item(Appetizer("Papas", 5))

order4.show_order()
print(f"Total esperado: 23.9")
print(f"Total obtenido: {order4.calculate_total()}")


print("\n===== PRUEBA GETTERS Y SETTERS =====")

drink = Drink("Jugo", 6, "Mediano")
print(drink.get_name())
print(drink.get_price())
print(drink.get_size())

drink.set_name("Limonada")
drink.set_price(7)
drink.set_size("Grande")

print(drink.get_name())
print(drink.get_price())
print(drink.get_size())


print("\n===== PRUEBA PAYMENT =====")

total = order4.calculate_total()
payment = Payment(total)
payment.pay()