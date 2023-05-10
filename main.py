from abc import ABC, abstractmethod
import random

# Singleton pattern
class PizzaStore:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.pizza_pool = PizzaPool()
        return cls.__instance

    def order_pizza(self, pizza_type):
        pizza = self.pizza_pool.get_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

# Builder and Prototype patterns
class Pizza(ABC):
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.toppings = []

    def prepare(self):
        print(f"Preparing {self.name}")
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings:")
        for topping in self.toppings:
            print(f"   {topping}")

    def bake(self):
        print("Baking for 25 minutes at 350 degrees")

    def cut(self):
        print("Cutting into diagonal slices")

    def box(self):
        print("Placing pizza in official PizzaStore box")

    # Abstract Factory pattern
    @classmethod
    @abstractmethod
    def get_factory(cls):
        pass

# Concrete Pizza classes
class CheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Cheese Pizza"
        self.dough = "Regular crust"
        self.sauce = "Marinara sauce"
        self.toppings = ["Fresh mozzarella", "Parmesan"]

    # Factory Method pattern
    @classmethod
    def get_factory(cls):
        return CheesePizzaFactory()

class PepperoniPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Pepperoni Pizza"
        self.dough = "Thick crust"
        self.sauce = "Tomato sauce"
        self.toppings = ["Pepperoni", "Sausage", "Mushrooms"]

    # Factory Method pattern
    @classmethod
    def get_factory(cls):
        return PepperoniPizzaFactory()

# Abstract Factory classes
class PizzaFactory(ABC):
    @abstractmethod
    def create_pizza(self):
        pass

class CheesePizzaFactory(PizzaFactory):
    def create_pizza(self):
        return CheesePizza()

class PepperoniPizzaFactory(PizzaFactory):
    def create_pizza(self):
        return PepperoniPizza()

# Object Pooling pattern
class PizzaPool:
    def __init__(self):
        self.pool = {}

    def get_pizza(self, pizza_type):
        if pizza_type not in self.pool:
            print(f"Creating new {pizza_type} pizza")
            self.pool[pizza_type] = pizza_type.get_factory().create_pizza()
        else:
            print(f"Reusing existing {pizza_type} pizza")
        return self.pool[pizza_type]

# Example usage
pizza_store = PizzaStore()
for _ in range(5):
    pizza = pizza_store.order_pizza(random.choice([CheesePizza, PepperoniPizza]))
    print("-" * 50)
