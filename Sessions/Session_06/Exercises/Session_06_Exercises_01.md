# Exercises 06: Object-Oriented Programming (OOP) I

Welcome to the exercises for Session 06! This sheet will help you practice the basics of classes, objects, and the constructor method.

## 6.1: Introduction to OOP

1.  **Paradigms & Benefits:** Briefly explain the core difference between Procedural and Object-Oriented Programming. Name one major benefit of using OOP for large projects.
2.  **Digital Twin:** Give an example of a physical industrial component and list two **Attributes** and two **Methods** that its software "Digital Twin" might have.

## 6.2: Classes and Objects

1.  **Conventions & Basics:** Which of these class names follow PEP 8 (PascalCase): `temp_sensor`, `PressureSensor`, `motor`, `RobotArm`? 
2.  **Instantiation:** Define a class named `Machine` using the `pass` keyword. Create two instances named `m1` and `m2`, and use `isinstance()` to verify that `m1` is indeed a `Machine`.

## 6.3: Attributes and Methods

1.  **State vs. Behavior:** In the context of a `Pump` object, identify which are **Attributes** and which are **Methods**: `pressure`, `start()`, `rpm`, `stop()`, `is_running`.
2.  **Using `self`:** Define a class `RobotArm` with a method `move_to(self, position)`. The method should print: "Moving arm to [position]...". Create an object and call this method.

## 6.4: The `__init__` Method

1.  **The Constructor:** Define a class `Sensor` with an `__init__` method that accepts `sensor_type` and `location`. Store these as attributes and initialize a third attribute `value` to `0.0`. 
2.  **Validation & Lists:** 
    - Create a class `Product` with an `__init__` method that takes `serial_number` and `weight`. 
    - Raise a `ValueError` if the weight is less than or equal to zero.
    - Create a list of three `Product` objects and use a loop to print each product's serial number.