---
marp: true
theme: fhooe
header: Object-Oriented Programming (OOP) II
footer: Dr. Georg Hackenberg, Professor for Industrial Informatics
paginate: true
math: mathjax
---

<!-- Abstract illustration showing a family tree or hierarchy of glowing geometric shapes. -->

![bg right](./Images/Chapter.png)

# Chapter 7: Object-Oriented Programming (OOP) II

This chapter includes the following sections:

- 7.1: Inheritance
- 7.2: Polymorphism
- 7.3: Encapsulation
- 7.4: Abstract Classes

---

<!-- Illustration of a Russian Matryoshka doll or a tree structure showing parent-child relationships. -->

![bg right](./Images/Section_1.png)

## 7.1: Inheritance

Don't start from scratch. Build upon what exists.

- The DRY Principle
- Parent and Child Classes
- The `super()` Function
- Overriding vs Extending
- Practical Examples

---

### The DRY Principle

**DRY: Don't Repeat Yourself.**

Imagine you are coding a game.
- `Car` has speed, color, and can move.
- `Truck` has speed, color, and can move.
- `Motorcycle` has speed, color, and can move.

Writing the same code 3 times is bad. If you fix a bug in `Car.move()`, you have to fix it in `Truck` and `Motorcycle` too.

**Inheritance** solves this.

---

<div class="columns">
<div class="two">

### The Concept of Inheritance

Inheritance allows us to define a generic **Parent Class** (Base Class) and generic methods once.

**Child Classes** (Derived Classes) inherit all attributes and methods from the Parent.

- **Vehicle** (Parent)
    - `Car` (Child)
    - `Truck` (Child)
    - `Motorcycle` (Child)

</div>
<div>

<div class="mermaid">
classDiagram
    Vehicle <|-- Car
    Vehicle <|-- Truck
    Vehicle <|-- Motorcycle
    class Vehicle {
        +speed
        +color
        +move()
    }
</div>

</div>
</div>

---

<div class="columns">
<div class="two">

### Defining Inheritance

Syntax: `class Child(Parent):`

```python
# Parent Class (Base Class)
class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print(f"{self.brand} is moving.")

# Child Class (Derived Class)
class Car(Vehicle):
    # Car inherits everything from Vehicle!
    pass

c = Car("Toyota")
c.drive() # Output: Toyota is moving.
```

</div>
<div>

![Diagram showing Vehicle class at top, pointing down to Car and Truck classes. (Mermaid)](./Diagrams/Mermaid/inheritance_vehicle.svg)

</div>
</div>

---

### The `is-a` Relationship

Inheritance models an **"is-a"** relationship.

- A Car **is a** Vehicle.
- A Manager **is an** Employee.
- A Square **is a** Shape.

If you cannot say "X is a Y", you probably shouldn't use inheritance. (e.g., A Car has a Wheel, but a Car *is not* a Wheel. Use composition instead.)

---

### Adding Specific Functionality

Child classes are not just copies. They can have their own specific methods.

```python
class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

class Truck(Vehicle):
    def load_cargo(self):
        print("Loading heavy cargo...")

c = Car("BMW")
c.drive()     # Inherited
c.honk()      # Specific to Car

t = Truck("Volvo")
t.drive()     # Inherited
t.load_cargo()# Specific to Truck
# t.honk()    # Error! Truck has no honk.
```

---

### Overriding Methods

Sometimes the parent's behavior isn't quite right for the child. The child can **Override** (replace) the method.

```python
class Vehicle:
    def drive(self):
        print("Vehicle moving...")

class ElectricCar(Vehicle):
    # Same method name as Parent -> Overrides it
    def drive(self):
        print("Electric Car moving silently...")

v = Vehicle()
v.drive() # Vehicle moving...

e = ElectricCar("Tesla")
e.drive() # Electric Car moving silently...
```

---

<div class="columns">
<div>

### The `super()` Function

Often, you don't want to *replace* the parent completely, but *extend* it.

`super()` gives you a reference to the Parent class.

Commonly used in `__init__`.

```python
class Robot:
    def __init__(self, name):
        self.name = name

class FlyingRobot(Robot):
    def __init__(self, name, wingspan):
        # 1. Let Parent handle the name
        super().__init__(name)
        # 2. Handle specific stuff
        self.wingspan = wingspan
```

</div>
<div>

<div class="mermaid">
sequenceDiagram
    participant Main
    participant Child as FlyingRobot
    participant Parent as Robot
    Main->>Child: FlyingRobot("Icarus", 50)
    Child->>Parent: super().__init__("Icarus")
    Parent-->>Child: Name set
    Child-->>Child: Wingspan set
    Child-->>Main: Return Object
</div>

</div>
</div>

---

### Why use `super()`?

1.  **Code Reuse:** You don't have to re-type `self.name = name` in every child class.
2.  **Maintainability:** If the Parent's `__init__` logic changes (e.g., adding an ID generation), all children get the update automatically.

---

<div class="columns">
<div class="two">

### Engineering Example: Sensors

We have a generic `Sensor` and a specific `TempSensor`.

```python
class Sensor:
    def __init__(self, id):
        self.id = id
        self.status = "OK"

    def log(self):
        print(f"Sensor {self.id}: {self.status}")

class TempSensor(Sensor):
    def read_temp(self):
        return 24.5 # Simulated

ts = TempSensor("T-101")
ts.log()        # Inherited from Sensor
print(ts.read_temp()) # Specific to TempSensor
```

</div>
<div>

<div class="mermaid">
classDiagram
    Sensor <|-- TempSensor
    class Sensor {
        +id
        +status
        +log()
    }
    class TempSensor {
        +read_temp() float
    }
</div>

</div>
</div>

---

### The `object` Class

In Python 3, all classes inherit from a built-in base class called `object`, even if you don't specify it.

`class Robot:` is actually `class Robot(object):`.

This is why every object comes with built-in methods like `__str__`, `__eq__`, etc.

---

<!-- Illustration of shapes (circle, square, triangle) fitting into the same hole or interface. -->

![bg right](./Images/Section_2.png)

## 7.2: Polymorphism

Many forms, one interface.

- What is Polymorphism?
- Treating objects uniformly
- "Duck Typing"
- Polymorphism in Functions
- Practical Simulation Example

---

### What is Polymorphism?

**Polymorphism** (Greek: "many forms") means that different classes can be used through the same **Interface**.

If `Car`, `Boat`, and `Plane` all have a `move()` method, I don't need to know which one I have. I just call `.move()`, and the object does the right thing.

---

<div class="columns">
<div class="two">

### Polymorphism in Action

```python
class Car:
    def move(self):
        print("Driving on road")

class Boat:
    def move(self):
        print("Sailing on water")

# List of different objects
vehicles = [Car(), Boat(), Car()]

# The loop doesn't care about the type!
for v in vehicles:
    v.move()
```

<div class="mermaid">
flowchart LR
    L[Loop: for v in vehicles] --> C{v.move()}
    C -->|v is Car| M1[Run Car.move]
    C -->|v is Boat| M2[Run Boat.move]
    M1 --> N[Next Iteration]
    M2 --> N
</div>

**Output:**
Driving on road
Sailing on water
Driving on road

</div>
<div>

![Illustration of a universal remote control operating different devices (TV, Stereo, AC).](./Images/Polymorphism_Remote.jpg)

</div>
</div>

---

### "Duck Typing"

Python is a dynamic language. It uses **Duck Typing**:

> "If it walks like a duck and quacks like a duck, then it must be a duck."

Python does not check "Is this object a Child of Vehicle?".
It checks "Does this object have a `.move()` method?"

If yes, it runs. If no, it crashes (`AttributeError`).

---

### Polymorphism in Functions

Functions can accept any object that satisfies the expected interface.

```python
def start_trip(vehicle):
    # This function works with ANY object
    # that has a move() method.
    print("Starting trip...")
    vehicle.move()
    print("Trip ended.")

c = Car()
b = Boat()

start_trip(c) # Works!
start_trip(b) # Works!
```

---

<div class="columns">
<div class="two">

### Engineering Example: Simulation Loop

Imagine simulating a factory. Every machine has a `step()` function.

```python
class Conveyor:
    def step(self):
        print("Conveyor: Moving items...")

class RobotArm:
    def step(self):
        print("Arm: Welding...")

machines = [Conveyor(), RobotArm(), Conveyor()]

print("--- Step 1 ---")
for m in machines:
    m.step() 
```

</div>
<div>

<div class="mermaid">
classDiagram
    direction LR
    class Conveyor {
        +step()
    }
    class RobotArm {
        +step()
    }
    note "Polymorphism: Both implement step()"
</div>

</div>
<div>

![Diagram of a simulation loop iterating over a list of generic Machine objects. (Mermaid)](./Diagrams/Mermaid/simulation_loop.svg)

</div>
</div>

---

<!-- Illustration of a capsule or a safe, symbolizing protected contents. -->

![bg right](./Images/Section_3.png)

## 7.3: Encapsulation

Protecting the inner workings.

- Why Hide Data?
- Public, Protected, Private
- Name Mangling
- Getters and Setters
- Properties (`@property`)

---

### The Public Interface

An object should present a clean **Interface** (methods) to the world, but hide its **Implementation** (data).

**Why?**
1.  **Safety:** Prevent invalid data (e.g., `speed = -100`).
2.  **Simplicity:** The user doesn't need to know how the engine works, just where the gas pedal is.
3.  **Flexibility:** You can change the internal code later without breaking other people's code.

---

### Access Modifiers in Python

Unlike Java or C++, Python does not enforce strict privacy. It relies on **Naming Conventions**.

| Level | Syntax | Meaning |
| :--- | :--- | :--- |
| **Public** | `name` | Accessible from anywhere. Normal use. |
| **Protected** | `_name` | "Internal use only". Please don't touch from outside. |
| **Private** | `__name` | Hard to access. Implementation detail. |

---

### Public vs Protected

```python
class Account:
    def __init__(self):
        self.balance = 100    # Public
        self._pin = 1234      # Protected

a = Account()

print(a.balance) # OK: 100

# This works, but VS Code will warn you,
# and other developers will frown at you.
print(a._pin)    # 1234 
```

**Rule:** If you see `_variable`, treat it as private.

---

### Private Members

Double underscores (`__`) trigger **Name Mangling**. Python changes the variable name internally to make it harder to access.

```python
class Secret:
    def __init__(self):
        self.__code = "Top Secret"

s = Secret()

# print(s.__code) 
# AttributeError: 'Secret' object has no attribute '__code'
```

It's not truly secure (you can access it via `_Secret__code`), but it prevents accidental access.

---

### Getters and Setters (The Old Way)

In languages like Java, you write `get_speed()` and `set_speed()` methods to control access.

```python
class Motor:
    def __init__(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed < 0:
            print("Error: Negative speed.")
        else:
            self.__speed = speed
```
This works, but it's "un-Pythonic" (verbose).

---

### The Pythonic Way: `@property`

Python allows you to use methods as if they were attributes!

```python
class Motor:
    def __init__(self):
        self._speed = 0

    @property         # The Getter
    def speed(self):
        return self._speed

    @speed.setter     # The Setter
    def speed(self, value):
        if value < 0:
            print("Error!")
        else:
            self._speed = value
```

---

<div class="columns">
<div>

### Using Properties

To the user, `speed` looks like a variable. But underneath, it runs your methods!

```python
m = Motor()

# Calls the setter
m.speed = 100 
print("Set to 100")

# Calls the setter (Validation logic runs!)
m.speed = -50 
# Output: Error!

# Calls the getter
print(m.speed) # Output: 100 (Still)
```

</div>
<div>

<div class="mermaid">
sequenceDiagram
    participant User
    participant Setter as @speed.setter
    participant Data as self._speed
    User->>Setter: m.speed = 100
    Setter->>Data: _speed = 100
    User->>Setter: m.speed = -50
    Setter--xUser: Print "Error!" (Data unchanged)
</div>

<div class="mermaid">
classDiagram
    class Motor {
        -int _speed
        +speed() int
        +speed(value) void
    }
</div>

</div>
</div>

---

### Read-Only Attributes

If you define a `@property` getter but **no** setter, the attribute becomes read-only.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        # Calculated on the fly
        return 3.14 * self.radius ** 2

c = Circle(10)
print(c.area) # 314.0

# c.area = 50 
# AttributeError: can't set attribute
```

---

<!-- Illustration of a transparent blueprint or a ghost outline. -->

![bg right](./Images/Section_4.png)

## 7.4: Abstract Classes

Blueprints for blueprints.

- The Concept of Abstraction
- The `abc` Module
- Abstract Methods
- Enforcing Interfaces
- Engineering Example

---

### The Concept of Abstraction

Sometimes, a Parent Class is so generic that it shouldn't exist as an object.

**Example: `Shape`**
- What is the area of a "Shape"? It depends.
- You can't calculate it until you know if it's a Circle or Square.
- `Shape` is an **Abstract Concept**.

We want to enforce that *every* child of `Shape` *must* implement an `area()` method.

---

### Abstract Base Classes (ABCs)

Python provides the `abc` module to create Abstract Classes.

1.  Inherit from `ABC`.
2.  Use the `@abstractmethod` decorator.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass 
        # No implementation. Just a rule.
```

---

### Enforcing Rules

```python
# 1. You cannot instantiate the Abstract Class
# s = Shape() 
# TypeError: Can't instantiate abstract class...

# 2. Child classes MUST implement abstract methods
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    # If we forget to define area(), this class 
    # will ALSO be abstract and cannot be instantiated.
    def area(self):
        return self.side * self.side

sq = Square(5) # This works!
```

---

### Why use Abstract Classes?

1.  **Guarantees:** You know for sure that any `Shape` object has an `area()` method.
2.  **Design:** It forces you to think about the "Contract" or "Interface" of your system before writing details.
3.  **Teamwork:** One person defines the Interface (`PLCDriver`), others implement specific versions (`SiemensDriver`, `AllenBradleyDriver`).

---

<div class="columns">
<div>

### Engineering Example: Universal Driver

Imagine writing a control system that talks to different PLCs.

```python
class PLCDriver(ABC):
    @abstractmethod
    def connect(self, ip): pass
        
    @abstractmethod
    def read_register(self, addr): pass

class SiemensDriver(PLCDriver):
    def connect(self, ip):
        print(f"Connecting to S7 at {ip}")
    def read_register(self, addr):
        return 0 # Real logic here

def startup(driver: PLCDriver):
    # We are 100% sure 'driver' has .connect()
    driver.connect("192.168.0.1")
```

</div>
<div>

<div class="mermaid">
sequenceDiagram
    participant Main
    participant Func as startup()
    participant Siemens as SiemensDriver
    Main->>Func: startup(my_siemens_driver)
    Func->>Siemens: connect("192.168.0.1")
    Siemens-->>Func: Connected
    Func-->>Main: Done
</div>

<div class="mermaid">
classDiagram
    direction LR
    class PLCDriver {
        <<Abstract>>
        +connect(ip)*
        +read_register(addr)*
    }
    class SiemensDriver {
        +connect(ip)
        +read_register(addr)
    }
    PLCDriver <|-- SiemensDriver
</div>

</div>
</div>

---

### Exercises: Inheritance

1.  Create a class `Employee` with `name` and `salary`.
2.  Create a child class `Manager` that inherits from `Employee`.
3.  Add a `department` attribute to `Manager`.
4.  Override a `show_info()` method to display name, salary, and department.

---

### Exercises: Polymorphism

1.  Create classes `Cat` ("Meow") and `Dog` ("Woof") with a `speak()` method.
2.  Create a list `animals = [Cat(), Dog(), Cat()]`.
3.  Loop through the list and make them all speak.

---

### Exercises: Encapsulation

1.  Create a `BankVault` class.
2.  Add a private attribute `__secret_code` (e.g., "1234").
3.  Add a method `unlock(guess)` that prints "Open!" if the guess matches, or "Alarm!" otherwise.
4.  Try to access `__secret_code` directly and see the error.

---

### Exercises: Abstract Classes

1.  Define an abstract class `Appliance` with an abstract method `turn_on()`.
2.  Create a `Fan` class that prints "Fan spinning...".
3.  Create a `Light` class that prints "Light glowing...".
4.  Verify that you cannot create an `Appliance` object directly.

---

# Chapter 7: Summary

- **Inheritance (`class Child(Parent)`)**: Build new classes on top of existing ones. DRY principle.
- **`super()`**: Access parent methods from the child.
- **Polymorphism**: Different objects, same interface. "Duck Typing".
- **Encapsulation**: Hide internal state using `_` and `__`.
- **Properties (`@property`)**: The Pythonic way to control access (Getters/Setters).
- **Abstract Classes (`ABC`)**: Define templates and enforce implementation rules.
