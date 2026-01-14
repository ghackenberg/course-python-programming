# Exercises 07: Object-Oriented Programming (OOP) II

Welcome to the exercises for Session 07! This sheet covers the advanced pillars of OOP: Inheritance, Polymorphism, Encapsulation, and Abstraction.

## 7.1: Inheritance

1.  **The "Is-a" Rule:** For each pair, decide if Inheritance (is-a) is appropriate. If not, suggest a better relationship:
    -   `Truck` and `Vehicle`
    -   `Engine` and `Car`
    -   `Square` and `Shape`
2.  **The `super()` Function:** Define a parent class `Device` that takes a `brand` in its constructor. Create a child class `Sensor` that adds a `unit` attribute (e.g., "Celsius"). Use `super()` in the `Sensor` constructor to initialize the brand.

## 7.2: Polymorphism

1.  **Uniform Interface:** Create two classes, `Motor` and `Lamp`, each with a method `turn_off()`. Write a function `shut_down(items)` that loops through a list of these objects and calls `turn_off()` on each.
2.  **Duck Typing:** Explain in one sentence what "Duck Typing" means in Python and why it makes polymorphism more flexible than in strictly typed languages.

## 7.3: Encapsulation

1.  **Access Modifiers:** Explain the difference in naming convention and intended use between a **Public**, **Protected** (`_`), and **Private** (`__`) attribute in Python.
2.  **The `@property` Decorator:** Create a class `Tank` with a protected attribute `_level`. Use `@property` and a setter for `level` to ensure the value is always between 0 and 100. Raise a `ValueError` for invalid inputs.

## 7.4: Abstract Classes (ABC)

1.  **The Contract:** Use the `abc` module to create an abstract class `Tool(ABC)` with an abstract method `use()`. Explain why you cannot create an instance of `Tool` directly.
2.  **Implementation:** Create a concrete class `Hammer` that inherits from `Tool` and implements the `use()` method. Verify it works by instantiating a `Hammer` object and calling its method.

## 7.5: Composition

1.  **Modular Design:** Create a `Robot` class that **has a** `Battery` object as an attribute (Composition). Add a method to `Robot` that prints the battery's charge status by accessing the internal battery object.
2.  **Design Choice:** Briefly explain one advantage of using Composition (has-a) over Inheritance (is-a) when modeling a complex device like a smartphone.
