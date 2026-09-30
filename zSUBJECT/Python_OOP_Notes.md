# Python Object-Oriented Programming — Complete Study Notes

Adapted from your C++ OOP notes. Examples use simple Python syntax, short comments, and expected outputs. Each Python code block is a separate runnable example; copy one block into a `.py` file and run it. No third-party packages are required.

## Contents

1. [Classes, objects, and self](#1-classes-objects-and-self)
2. [Access conventions](#2-access-conventions)
3. [Encapsulation and properties](#3-encapsulation-and-properties)
4. [Abstraction and abstract classes](#4-abstraction-and-abstract-classes)
5. [Inheritance and its types](#5-inheritance-and-its-types)
6. [Polymorphism and duck typing](#6-polymorphism-and-duck-typing)
7. [Function overloading and overriding](#7-function-overloading-and-overriding)
8. [Operator overloading](#8-operator-overloading)
9. [Object creation and cleanup](#9-object-creation-and-cleanup)
10. [Composition, aggregation, and association](#10-composition-aggregation-and-association)
11. [Assignment, shallow copy, and deep copy](#11-assignment-shallow-copy-and-deep-copy)
12. [Class attributes and method types](#12-class-attributes-and-method-types)
13. [Diamond inheritance, MRO, and super](#13-diamond-inheritance-mro-and-super)
14. [Memory management](#14-memory-management)
15. [Generics and type hints](#15-generics-and-type-hints)
16. [C++ features without direct Python equivalents](#16-c-features-without-direct-python-equivalents)
17. [Useful Python OOP features](#17-useful-python-oop-features)
18. [Complete vehicle example](#18-complete-vehicle-example)
19. [Time and space complexity](#19-time-and-space-complexity)
20. [Revision sheet and common mistakes](#20-revision-sheet-and-common-mistakes)

## 1. Classes, objects, and self

**OOP** organizes related data and behavior into objects.

- **Class:** defines the attributes and methods its objects can use.
- **Object / instance:** a particular instance of a class.
- **Attribute:** data attached to an object or class.
- **Method:** a function defined on a class.
- **`self`:** the current instance, similar in purpose to C++ `this`.
- **`__init__`:** initializes an instance after it has been created.

Use classes when state and operations belong together—for example, an account and its deposit operation. A small stateless calculation can remain a plain function.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name      # Attribute belonging to this student.
        self.marks = marks

    def display(self):
        print(f"{self.name}: {self.marks}")


student1 = Student("Janesh", 90)
student2 = Student("Alice", 85)

student1.display()  # Janesh: 90
student2.display()  # Alice: 85

student1.marks = 95
print(student1.marks)  # 95
print(student2.marks)  # 85 — a different object's attribute.
```

For this ordinary instance method, `student1.display()` is equivalent to `Student.display(student1)`. Python supplies the instance automatically when you call through the object; you declare the receiving `self` parameter explicitly.

`self.name = name` means: store the local parameter `name` as an attribute on this instance. `self` is a convention, not a reserved keyword, but always use that name for clarity.

## 2. Access conventions

Python does **not** enforce C++-style `public`, `protected`, and `private` access sections.

| Form | Meaning | Outside access |
|---|---|---|
| `name` | Public interface | Normal and intended |
| `_name` | Internal/nonpublic by convention | Possible; callers should avoid relying on it |
| `__name` | Name-mangled to reduce accidental subclass collisions | Possible through the mangled name |
| `__name__` | Special-method naming convention | Not a private-member convention |

```python
class Example:
    def __init__(self):
        self.public_value = 30
        self._internal_value = 20
        self.__private_value = 10

    def show_values(self):
        print(self.public_value, self._internal_value, self.__private_value)


class Derived(Example):
    def show_internal(self):
        print(self._internal_value)


obj = Example()
obj.show_values()                  # 30 20 10
print(obj.public_value)             # 30
Derived().show_internal()           # 20

# obj.__private_value would raise AttributeError.
print(obj._Example__private_value)  # 10 — possible, but avoid doing this.
```

Python rewrites `__private_value` inside `Example` to `_Example__private_value`. This is **name mangling**, not a security boundary. A subclass using its own `__private_value` gets a different mangled name.

## 3. Encapsulation and properties

**Encapsulation** groups data with the operations that manage it and gives callers a controlled interface. It helps preserve rules such as “balance must not be negative.”

`@property` lets a method be accessed like an attribute. A property setter can validate assignments.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance  # Calls the setter below.

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance = self.balance + amount


account = BankAccount(100)
account.deposit(50)
print(account.balance)  # 150 — no parentheses when reading a property.

try:
    account.balance = -10
except ValueError as error:
    print(error)        # Balance cannot be negative.
```

The property is the intended interface; `_balance` remains accessible by convention. This teaching example permits setting any nonnegative balance. A real account interface would normally expose specific transaction operations instead.

**Read-only property:** define the getter without a setter. Assignment through that property then fails, although that does not make every part of the object immutable.

## 4. Abstraction and abstract classes

**Abstraction** exposes what an operation does while keeping its implementation behind an interface. Calling `shape.area()` does not require the caller to know the formula.

An abstract base class can declare required operations using `ABC` and `@abstractmethod`.

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Concrete subclasses must provide an implementation.


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


for shape in [Rectangle(4, 5), Square(3)]:
    print(shape.area())  # 20, then 9

# Shape() would raise TypeError: area is still abstract.
```

A subclass that still has an unimplemented abstract method cannot be instantiated. Abstract classes can also have ordinary methods, instance attributes, and `__init__` methods. An abstract method may even contain reusable implementation code.

| Encapsulation | Abstraction |
|---|---|
| Organizes and controls access to state and behavior | Provides an interface that hides implementation details |
| “Use deposit to update this balance correctly” | “Call area without knowing the shape's formula” |

Abstraction does not require an abstract class; ordinary functions and classes can also expose simple interfaces.

## 5. Inheritance and its types

**Inheritance** lets a child class reuse or specialize a parent's behavior. Prefer it for an **is-a** relationship: a dog is an animal.

### Single inheritance and initialization

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize the parent part in this hierarchy.
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks")


dog = Dog("Bruno", "Labrador")
dog.eat()   # Bruno is eating
dog.bark()  # Bruno barks
```

If the child does not define `__init__`, it can inherit the parent's initializer. If it defines its own, the parent's initializer is not automatically run: call `super().__init__(...)` when needed.

### The five inheritance forms

| Type | Meaning | Python form |
|---|---|---|
| Single | One parent | `class Dog(Animal)` |
| Multiple | More than one direct parent | `class Labrador(Dog, Domestic)` |
| Multilevel | A chain of inheritance | `Animal`, then `Dog(Animal)`, then `Puppy(Dog)` |
| Hierarchical | Several children of one parent | `Dog(Animal)` and `Cat(Animal)` |
| Hybrid | A combination of forms | A hierarchy combining multiple and multilevel inheritance |

```python
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):                # Single inheritance.
    def bark(self):
        print("Barking")


class Puppy(Dog):                # Multilevel inheritance.
    pass


class Cat(Animal):               # Dog and Cat form hierarchical inheritance.
    pass


class Domestic:
    def is_pet(self):
        print("I am a pet")


class Labrador(Dog, Domestic):   # Multiple inheritance; overall a hybrid.
    pass


Puppy().bark()       # Barking
Cat().eat()          # Eating
lab = Labrador()
lab.eat()           # Eating
lab.is_pet()        # I am a pet
```

`pass` is a placeholder that does nothing. These subclasses still inherit behavior.

## 6. Polymorphism and duck typing

**Polymorphism** lets the same operation behave differently for different objects.

### Overriding through inheritance

```python
class Animal:
    def speak(self):
        return "Animal sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


for animal in [Dog(), Cat()]:
    print(animal.speak())  # Woof, then Meow
```

No `virtual` keyword is required. Ordinary method lookup selects the implementation based on the actual object and its class hierarchy.

### Duck typing: inheritance is optional

```python
class PDFPrinter:
    def print_document(self):
        return "Printing PDF"


class PhotoPrinter:
    def print_document(self):
        return "Printing photo"


def start_printing(printer):
    # Any object supporting this operation can be used.
    print(printer.print_document())


start_printing(PDFPrinter())    # Printing PDF
start_printing(PhotoPrinter())  # Printing photo
```

The function needs a compatible `print_document()` method, not a shared parent. Passing an incompatible object would fail when the missing or incompatible operation is used.

## 7. Function overloading and overriding

### Python does not select ordinary methods by signature

In C++, you can define several `add` methods with different parameter lists. In a Python class body, defining the same name again replaces the earlier definition.

```python
class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c  # This is the surviving definition.


calculator = Calculator()
print(calculator.add(1, 2, 3))  # 6
# calculator.add(1, 2) would raise TypeError: missing argument c.
```

### Use defaults or variable arguments

```python
class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

    def add_many(self, *numbers):
        # *numbers collects positional arguments into a tuple.
        return sum(numbers)


calculator = Calculator()
print(calculator.add(2, 3))         # 5
print(calculator.add(2, 3, 4))      # 9
print(calculator.add_many(1, 2, 3, 4))  # 10
```

`typing.overload` can describe multiple signatures for static type checking, but it does not create runtime dispatch. You still supply one runtime implementation. Python operator overloading is also not C++ compile-time overload resolution.

### Overriding and incompatible signatures

```python
class Base:
    def show(self):
        print("Base show")


class Derived(Base):
    def show(self, value):
        print("Derived show:", value)

    def show_base(self):
        super().show()  # Explicitly use the next implementation in the MRO.


obj = Derived()
obj.show(5)      # Derived show: 5
obj.show_base()  # Base show
# obj.show() would raise TypeError; Python does not retry Base.show().
```

Changing the required arguments can break code expecting the parent's interface. Keep overriding methods compatible with the calls their parent supports.

## 8. Operator overloading

Special methods let your objects work with operators such as `+` and `==`.

| Syntax | Relevant method | Purpose |
|---|---|---|
| `a + b` | `__add__` | Addition |
| `a - b` | `__sub__` | Subtraction |
| `a == b` | `__eq__` | Value equality |
| `a < b` | `__lt__` | Less-than comparison |
| `len(a)` | `__len__` | Length |
| `print(a)` / `str(a)` | `__str__` | User-facing text |
| `repr(a)` | `__repr__` | Developer-facing representation |

```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            return NotImplemented  # Let Python try supported alternatives.
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __repr__(self):
        return f"ComplexNumber({self.real!r}, {self.imag!r})"


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 4)
result = a + b
print(result)        # 4 + 6i
print(repr(result))  # ComplexNumber(4, 6)
```

`NotImplemented` is a special return value, not the `NotImplementedError` exception. For addition it lets Python try reflected dispatch, such as the other operand's `__radd__`; if neither operand supports the operation, Python raises `TypeError`.

## 9. Object creation and cleanup

### `__new__` creates; `__init__` initializes

In normal construction, `ClassName(...)` invokes `__new__` to create an instance, then `__init__` to initialize it. Most application classes only need `__init__`.

```python
class Example:
    def __new__(cls, value):
        print("1. Creating the object")
        return super().__new__(cls)

    def __init__(self, value):
        print("2. Initializing the object")
        self.value = value


obj = Example(10)
print(obj.value)  # 10
```

`cls` refers to the class, while `self` refers to an instance. `__init__` must return `None`, usually by having no explicit return statement.

### `__del__` is not deterministic C++ destruction

Python has a finalizer named `__del__`, but you should not depend on its timing for resource cleanup. `del obj` removes a reference; it does not guarantee immediate destruction. Finalizers may run during interpreter shutdown, and execution at shutdown is not guaranteed for every surviving object.

Use a context manager for resources that must be released promptly.

```python
from io import StringIO


class TextSession:
    def __enter__(self):
        self.buffer = StringIO()
        print("Opened")
        return self.buffer  # Bound to 'buffer' in the with statement.

    def __exit__(self, exc_type, exc_value, traceback):
        self.buffer.close()
        print("Closed")
        return False  # Do not suppress an exception from the with block.


with TextSession() as buffer:
    buffer.write("Hello")
    print(buffer.getvalue())  # Hello

print(buffer.closed)         # True
# Output sequence: Opened, Hello, Closed, True.
```

After a successful `__enter__`, `__exit__` runs when the block exits normally or through an exception. For files, the built-in pattern is `with open(...) as file:`.

## 10. Composition, aggregation, and association

These are design relationships, not different Python access keywords.

| Relationship | Meaning | Example |
|---|---|---|
| Composition | A whole creates/manages its parts as part of its design | House has rooms |
| Aggregation | A whole groups independently existing objects | School has students |
| Association | Objects interact or know about each other | Doctor visits hospital |

```python
class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self):
        self.room = Room("Bedroom")  # Composition: creates its own part.


class Student:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self):
        self.students = []

    def enroll(self, student):
        self.students.append(student)  # Aggregation: keeps an existing object.


class Hospital:
    def __init__(self, name):
        self.name = name


class Doctor:
    def visit(self, hospital):
        print(f"Visiting {hospital.name}")  # Association.


house = House()
print(house.room.name)  # Bedroom

student = Student("Alice")
school = School()
school.enroll(student)
del school
print(student.name)     # Alice — student still exists.

Doctor().visit(Hospital("City Hospital"))  # Visiting City Hospital
```

Python does not enforce UML lifetime rules. Even a composition part can remain alive if another reference to it exists. Likewise, “weak ownership” in a design description does not automatically mean a Python `weakref`; the school's list above holds ordinary strong references.

Prefer composition when the relationship is **has-a**, such as a car having an engine. Do not inherit just to reuse a few unrelated methods.

## 11. Assignment, shallow copy, and deep copy

| Operation | New outer object? | Nested mutable objects |
|---|---|---|
| `b = a` | No | Same object throughout |
| `copy.copy(a)` | Yes, for this normal user-defined object | Shared references |
| `copy.deepcopy(a)` | Yes, for this example | Recursively copied |

```python
import copy


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


a = Student("Alice", [80, 90])
alias = a
shallow = copy.copy(a)
deep = copy.deepcopy(a)

print(alias is a)    # True
print(shallow is a)  # False

a.marks.append(100)
print(alias.marks)    # [80, 90, 100]
print(shallow.marks)  # [80, 90, 100] — shares the list.
print(deep.marks)     # [80, 90] — separate list.

a.name = "Bob"
print(alias.name)    # Bob — same outer object.
print(shallow.name)  # Alice — separate outer object.
```

Shallow copying is not inherently unsafe, and Python references do not need manual `delete` calls. Deep copying is useful when nested mutable state should be independent, but it costs more and is not appropriate for every resource. Some objects are shared or unsupported by deep copying, and classes can customize copying behavior.

`is` checks whether two references point to the same object. `==` checks equality according to the object's equality behavior.

## 12. Class attributes and method types

An **instance attribute** belongs to one instance. A **class attribute** is stored on the class and can be shared through attribute lookup.

| Method | First automatic argument | Typical use |
|---|---|---|
| Instance method | `self` | Read or change an instance |
| `@classmethod` | `cls` | Alternate constructor or class-level behavior |
| `@staticmethod` | None | Utility logically grouped with a class |

```python
class Employee:
    company = "Example Corp"  # Class attribute.
    total_created = 0

    def __init__(self, name):
        self.name = name      # Instance attribute.
        Employee.total_created += 1

    def describe(self):
        return f"{self.name} works at {self.company}"

    @classmethod
    def from_text(cls, text):
        return cls(text.strip())  # Constructs the class on which it is called.

    @staticmethod
    def is_valid_name(name):
        return bool(name.strip())


a = Employee("Alice")
b = Employee.from_text(" Bob ")
print(a.describe())                 # Alice works at Example Corp
print(b.name)                       # Bob
print(Employee.total_created)       # 2 (created, not currently alive)
print(Employee.is_valid_name(" "))  # False

a.company = "Other Corp"            # Creates an instance attribute.
print(a.company)                    # Other Corp
print(b.company)                    # Example Corp
print(Employee.company)             # Example Corp
```

A static method has no automatic access to `self` or `cls`, but it can access explicitly supplied objects or explicitly named classes. It is not restricted to static data by the language.

### Avoid accidentally shared mutable class data

```python
class Team:
    def __init__(self):
        self.members = []  # A new list for every instance.


a = Team()
b = Team()
a.members.append("Alice")
print(a.members)  # ['Alice']
print(b.members)  # []
```

If `members = []` were in the class body, appending through different instances would modify the same inherited class list unless an instance had replaced that attribute.

## 13. Diamond inheritance, MRO, and super

A diamond occurs when `B` and `C` both inherit `A`, and `D` inherits both `B` and `C`.

Python uses **C3 method resolution order (MRO)** to define a consistent class lookup order. It does not create separate C++-style base subobjects or require virtual inheritance syntax.

```python
class A:
    def __init__(self):
        print("A")
        super().__init__()


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()


obj = D()  # Prints D, B, C, A.
print([cls.__name__ for cls in D.__mro__])
# ['D', 'B', 'C', 'A', 'object']
```

`super()` means **continue lookup after the current class in the MRO**, not always “call my direct parent.” In this example, `super()` inside `B` reaches `C` when acting on a `D` instance.

Cooperative methods call `super()` consistently and use compatible arguments. Directly calling both `B.__init__(self)` and `C.__init__(self)` can duplicate initialization work. Inconsistent hierarchies can be rejected with `TypeError`; MRO is not a fix for every multiple-inheritance design.

## 14. Memory management

Python variables hold references to objects. There is no ordinary C++ `new`/`delete` pair to manage.

```python
class Box:
    def __init__(self, value):
        self.value = value


a = Box(42)
b = a

del a          # Removes this name, not the reference held by b.
print(b.value)  # 42
```

CPython primarily uses reference counting together with cyclic garbage collection. Other Python implementations may manage memory differently. Unreachable objects can be reclaimed; do not base application correctness on the exact time of reclamation.

Function arguments also refer to objects. Mutating a passed object can affect the caller; rebinding the local parameter does not rebind the caller's variable. Passing an object does not automatically copy it.

## 15. Generics and type hints

C++ templates generate/type-check specialized code during compilation. Python often handles reusable operations through dynamic typing; type hints add information for readers and static checkers.

```python
def add(a, b):
    return a + b


print(add(3, 4))            # 7
print(add(2.5, 1.5))        # 4.0
print(add("Hello ", "OOP")) # Hello OOP
```

A typed generic class expresses a relationship between the stored and returned types:

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Storage(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value


number = Storage[int](100)
text = Storage[str]("Hello")
print(number.get_value())  # 100
print(text.get_value())    # Hello
```

Here `T` stands for a type chosen by the caller. Standard Python does not enforce these hints at runtime. A static checker can flag incorrect uses; annotations alone do not validate input values.

## 16. C++ features without direct Python equivalents

| C++ concept | Python approach | Important difference |
|---|---|---|
| `this->name` | `self.name` | Explicit instance parameter |
| Constructor | Usually `__init__` | `__new__` performs creation |
| Destructor / RAII | Context managers for resources | `__del__` timing is not deterministic |
| `private` / `protected` | `__name` / `_name` conventions | Not enforced C++ access control |
| `virtual` function | Ordinary overridable method | No `virtual` keyword needed |
| Pure virtual method | `ABC` and `@abstractmethod` | Prevents instantiation while abstract |
| Friend function | Function using the public interface | No `friend` keyword |
| Static member | Class attribute | Instance assignment may shadow it |
| Static function | `@staticmethod` | No automatic instance/class argument |
| V-table / vptr | Dynamic lookup and MRO | Do not assume C++ object layout |
| Virtual base class | Cooperative multiple inheritance and MRO | No separate virtual-base declaration |
| Function overloads | Defaults, `*args`, or explicit dispatch | Repeated definitions replace names |
| Templates | Dynamic operations and typed generics | Type hints do not specialize compiled code |
| `new` / `delete` | Object creation and automatic memory management | `del` removes a reference/binding |

### Friend-function alternative

```python
class Box:
    def __init__(self, width):
        self._width = width

    @property
    def width(self):
        return self._width


def display_width(box):
    print(box.width)  # Uses the public interface, no friend declaration.


display_width(Box(10))  # 10
```

For v-tables, learn Python's observable behavior: attribute lookup, bound methods, and MRO. A C++ v-table is not a Python language-level guarantee, and even C++ does not mandate one specific v-table layout.

## 17. Useful Python OOP features

### Dataclasses

`@dataclass` generates common methods such as `__init__`, `__repr__`, and value-based `__eq__` from declared fields. It is useful for classes primarily carrying data.

```python
from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    marks: list = field(default_factory=list)  # Separate list per student.


a = Student("Alice")
b = Student("Alice")
print(a)       # Student(name='Alice', marks=[])
print(a == b)  # True — matching field values.
print(a is b)  # False — separate instances.
a.marks.append(90)
print(b.marks) # []
```

### Instance and subclass checks

```python
class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(issubclass(Dog, Animal))  # True
print(type(dog) is Animal)     # False — exact type is Dog.
```

Use `isinstance` when subclasses should count. Duck-typed code often does not need an explicit type check at all.

### Method chaining

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self  # Return this same instance for another call.


counter = Counter()
counter.increment().increment()
print(counter.value)  # 2
```

## 18. Complete vehicle example

This adapts the vehicle example from your notes and adds a small fleet manager. It demonstrates abstraction, inheritance, encapsulation, polymorphism, composition, aggregation, and a class method.

```python
from abc import ABC, abstractmethod


class Engine:
    def start(self):
        return "engine started"


class Vehicle(ABC):
    def __init__(self, model):
        if not model.strip():
            raise ValueError("Model cannot be empty.")
        self._model = model

    @property
    def model(self):
        return self._model  # Read-only through this property.

    @classmethod
    def from_text(cls, text):
        return cls(text.strip())

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)
        self._engine = Engine()  # Composition: car creates its engine.

    def start_engine(self):
        return f"Car {self.model}: {self._engine.start()}"


class Bike(Vehicle):
    def __init__(self, model):
        super().__init__(model)
        self._engine = Engine()

    def start_engine(self):
        return f"Bike {self.model}: {self._engine.start()}"


class Fleet:
    def __init__(self):
        self._vehicles = []

    def add_vehicle(self, vehicle):
        self._vehicles.append(vehicle)  # Aggregation: accepts existing objects.

    def start_all(self):
        for vehicle in self._vehicles:
            # Polymorphism: each object provides its own implementation.
            print(vehicle.start_engine())


if __name__ == "__main__":
    car = Car.from_text(" Audi A5 ")
    bike = Bike("Yamaha")

    fleet = Fleet()
    fleet.add_vehicle(car)
    fleet.add_vehicle(bike)
    fleet.start_all()

    # Output:
    # Car Audi A5: engine started
    # Bike Yamaha: engine started
```

`Vehicle.from_text` uses `cls`, so calling `Car.from_text(...)` creates a `Car`. The fleet depends on the `start_engine()` operation; it does not need separate branches for cars and bikes.

## 19. Time and space complexity

OOP itself has no single complexity. Analyze the work and memory used by each method.

**Time complexity** describes how work grows with input size. **Extra space complexity** describes additional memory beyond existing input objects. The following assumes ordinary constant-cost primitive operations unless text length is specifically counted.

| Operation/example | Time | Additional space | Reason |
|---|---|---|---|
| Fixed numeric attribute update | O(1) | O(1) | Fixed amount of work |
| `ComplexNumber.__add__` above | O(1) | O(1) | Adds two pairs of fixed-size numbers; creates one object |
| `School.enroll` / `Fleet.add_vehicle` | O(1) amortized | List grows by one reference | List append occasionally resizes its backing array |
| `Calculator.add_many` with n numbers | O(n) | O(n) for the `*numbers` tuple | Collect and sum n arguments |
| Copy a flat list of n references | O(n) | O(n) | Allocate and populate another list |
| Deep-copy an ordinary nested container graph | O(V + E) | O(V + E) upper bound | Visit/copy objects V and references E; custom methods can change this |
| Store a fleet of n vehicles | O(n) total amortized additions | O(n) stored references | One entry per vehicle |
| Start all n vehicles | O(n + L) | O(M) temporary text | L is total text length produced; M is the longest message |

For a fixed-size message per vehicle, `start_all()` is O(n) time and O(1) extra temporary space, excluding the existing fleet and any external output buffering. It does not construct a list of all messages.

A property can perform arbitrary work: `obj.total` could be O(n) if its getter loops through n items. Short syntax is not evidence of constant time.

## 20. Revision sheet and common mistakes

| Question | Answer |
|---|---|
| What is a class? | A definition of attributes and behavior for instances |
| What is an object? | An instance with identity, state, and behavior |
| Four pillars? | Encapsulation, abstraction, inheritance, polymorphism |
| `self` versus `cls`? | Current instance versus class |
| `__init__` versus `__new__`? | Initialize an instance versus create it |
| Is `_value` protected? | It is nonpublic by convention, not enforced |
| Is `__value` inaccessible? | No; it is name-mangled |
| Does Python need `virtual`? | No, ordinary methods support overriding |
| Can the same name have two ordinary definitions? | The later definition replaces the earlier binding |
| Does `super()` always call the direct parent? | No; it follows the instance's class MRO |
| Is assignment a copy? | No; it binds another reference |
| Does `del obj` always destroy the object? | No; other references may keep it alive |
| When should resources be closed? | Explicitly or through a context manager |
| Are type hints runtime validation? | No |

Common mistakes to avoid:

1. Forgetting `self` in an instance method or using `name` when you mean `self.name`.
2. Putting a list in the class body when each instance needs its own list.
3. Using a mutable default argument such as `items=[]`; prefer `items=None` and initialize inside the method.
4. Defining multiple `__init__` methods and expecting signature-based selection; use defaults or class methods.
5. Replacing a parent's initializer without calling it when its state is required.
6. Treating name mangling as protection for secrets.
7. Assuming a shallow copy also duplicates every nested object.
8. Depending on `__del__` for timely file or connection cleanup.
9. Using `is` to compare ordinary string or numeric values; use `==` for value equality.
10. Using inheritance for a has-a relationship that composition represents more clearly.

Suggested study order: classes and `self` → attributes and methods → encapsulation → inheritance → polymorphism → abstraction → copying → method types → MRO → complete example.
