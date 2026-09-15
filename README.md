# Inheritance: Vehicle Types

Create a program that models several types of vehicles using a parent class and specialized child classes. Shared properties and behaviours should exist in the parent, while each child class adds or changes functionality that only makes sense for that vehicle type. This uses the “is-a” relationship, inherited functionality, overriding, and `super()` introduced in the inheritance slides. 

Requirements:

* Create a parent `Vehicle` class containing at least `make`, `model`, and `speed` properties and one method that can be used by every vehicle.
* Create at least two child classes, such as `Car`, `Motorcycle`, `Boat`, or another appropriate vehicle type. Each child must inherit from `Vehicle`.
* Each child class must add at least one property or method that does not exist in the parent class.
* Override one method from `Vehicle` in both child classes so that each vehicle type behaves differently when that method is called.
* Give each child its own `__init__()` method and use `super().__init__()` to initialize the properties inherited from `Vehicle`. Create at least one object from each child class and demonstrate both inherited and specialized behaviours.

The important relationship is that every child genuinely represents a more specific type of `Vehicle`, rather than simply being an object that happens to interact with one.

---

## File Structure

```text
vehicle_types/
│
├── vehicles.py
└── main.py
```

* `vehicles.py`

  * Contains the `Vehicle` parent class.
  * Contains all child vehicle classes.
  * Parent and child classes should not be defined in `main.py`.

* `main.py`

  * Imports the vehicle classes from `vehicles.py`.
  * Creates objects from at least two different child classes.
  * Demonstrates inherited methods, overridden methods, and features specific to each child class.
  * All code used to run and test the finished program should be placed here.

---

## Assessment

| Assessment Item                       | Criteria                                                                                                                                                     |  Marks |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -----: |
| ☐ `Vehicle` Parent Class              | Creates a `Vehicle` class containing `make`, `model`, and `speed` properties and at least one method that is appropriate for all vehicles.                   |      3 |
| ☐ Child Classes                       | Creates at least two different child classes that correctly inherit from `Vehicle`.                                                                          |      3 |
| ☐ Specialized Features                | Each child class adds at least one property or method that does not exist in the parent class and is appropriate for that vehicle type.                      |      3 |
| ☐ Method Overriding                   | Both child classes override the same inherited method with behaviour specific to that type of vehicle.                                                       |      4 |
| ☐ Using `super()`                     | Both child classes define their own `__init__()` methods and correctly use `super().__init__()` to initialize inherited properties.                          |      3 |
| ☐ Inherited and Specialized Behaviour | Creates objects from both child classes and demonstrates both functionality inherited from `Vehicle` and functionality belonging specifically to each child. |      2 |
| ☐ Complete Working Program            | The program runs without errors and the parent/child relationships clearly represent valid "is-a" relationships.                                             |      2 |
|                                       | **Total**                                                                                                                                                    | **20** |

