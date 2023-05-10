# **Pizza Store**

This is a Python program that implements several design patterns to simulate a pizza store. The following design patterns are used:

- Singleton: to ensure that only one instance of the PizzaStore class is created.
- Builder and Prototype: to build and clone Pizza objects with different attributes.
- Object Pooling: to reuse Pizza objects and avoid creating new ones unnecessarily.
- Factory Method and Abstract Factory: to create Pizza objects of different types.

**Usage**

To use the program, simply run the main.py script. This will create a PizzaStore instance and order several pizzas of random types. The pizzas will be prepared, baked, cut, boxed, and printed to the console.

**Design**

The program consists of the following classes:

- PizzaStore: a singleton class that represents a pizza store. It has a PizzaPool instance that manages the reuse of Pizza objects. It also has an order\_pizza method that orders a Pizza of a specified type.
- Pizza: an abstract base class that represents a pizza. It has methods for preparing, baking, cutting, and boxing a pizza, as well as an abstract get\_factory method that returns a factory for creating Pizza objects.
- CheesePizza and PepperoniPizza: concrete subclasses of Pizza that represent different types of pizzas. They implement the get\_factory method to return a factory for creating their respective types of Pizza objects.
- PizzaFactory: an abstract base class that represents a factory for creating Pizza objects. It has an abstract create\_pizza method that returns a new Pizza object.
- CheesePizzaFactory and PepperoniPizzaFactory: concrete subclasses of PizzaFactory that represent factories for creating CheesePizza and PepperoniPizza objects, respectively.
- PizzaPool: a class that manages the reuse of Pizza objects. It has a pool dictionary that maps Pizza types to their corresponding objects. It has a get\_pizza method that returns a Pizza of a specified type, either by reusing an existing object from the pool or by creating a new one using the factory returned by the Pizza type's get\_factory method.

**Limitations**

This program is a simplified simulation of a pizza store and does not handle all possible scenarios and edge cases. For example, it does not handle errors that may occur during pizza preparation, baking, cutting, or boxing. It also does not handle the case where the PizzaPool runs out of Pizza objects to reuse. Furthermore, it only implements two types of pizzas (CheesePizza and PepperoniPizza), and does not allow for the creation of new types of pizzas at runtime.