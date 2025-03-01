# Complete Object-Oriented Programming (OOP) in C++ – In-Depth Notes

## Table of Contents
- [Complete Object-Oriented Programming (OOP) in C++ – In-Depth Notes](#complete-object-oriented-programming-oop-in-c--in-depth-notes)
  - [Table of Contents](#table-of-contents)
  - [1. Introduction to OOP](#1-introduction-to-oop)
    - [What is OOP?](#what-is-oop)
    - [Why do we use OOP?](#why-do-we-use-oop)
  - [2. Access Specifiers in C++](#2-access-specifiers-in-c)
    - [Definition](#definition)
    - [Why do we use Access Specifiers?](#why-do-we-use-access-specifiers)
    - [Table of Access Specifiers](#table-of-access-specifiers)
    - [Complete Example](#complete-example)
  - [3. Four Pillars of OOP](#3-four-pillars-of-oop)
    - [3.1 Encapsulation](#31-encapsulation)
    - [3.2 Abstraction](#32-abstraction)
    - [3.3 Inheritance](#33-inheritance)
      - [Types of Inheritance](#types-of-inheritance)
    - [3.4 Polymorphism](#34-polymorphism)
  - [4. Constructor \& Destructor Execution Flow](#4-constructor--destructor-execution-flow)
    - [Definition](#definition-1)
    - [Why use them?](#why-use-them)
    - [Complete Example](#complete-example-1)
  - [5. Composition, Aggregation \& Association](#5-composition-aggregation--association)
    - [Definitions](#definitions)
    - [Why use them?](#why-use-them-1)
    - [Table Representation](#table-representation)
    - [Complete Examples](#complete-examples)
  - [6. Shallow Copy vs Deep Copy](#6-shallow-copy-vs-deep-copy)
    - [Definition](#definition-2)
    - [Why?](#why)
    - [Complete Example](#complete-example-2)
  - [7. Virtual Functions \& Abstract Classes](#7-virtual-functions--abstract-classes)
    - [Virtual Functions](#virtual-functions)
    - [Abstract Classes](#abstract-classes)
  - [8. Friend Function](#8-friend-function)
    - [Definition](#definition-3)
    - [Why?](#why-1)
    - [Complete Example](#complete-example-3)
  - [9. Static Members \& Functions](#9-static-members--functions)
    - [Definition](#definition-4)
    - [Why?](#why-2)
    - [Complete Example](#complete-example-4)
  - [10. This Pointer](#10-this-pointer)
    - [Definition](#definition-5)
    - [Why?](#why-3)
    - [Complete Example](#complete-example-5)
  - [11. V-Table \& V-Table Pointer](#11-v-table--v-table-pointer)
    - [Definition](#definition-6)
    - [Why?](#why-4)
    - [Complete Example](#complete-example-6)
  - [12. Diamond Problem \& Virtual Base Class](#12-diamond-problem--virtual-base-class)
    - [Definition: Diamond Problem](#definition-diamond-problem)
    - [Why is it a Problem?](#why-is-it-a-problem)
    - [Virtual Base Class](#virtual-base-class)
    - [Complete Example](#complete-example-7)
  - [13. Dynamic Memory Allocation in OOP](#13-dynamic-memory-allocation-in-oop)
    - [Definition](#definition-7)
    - [Why?](#why-5)
    - [Complete Example](#complete-example-8)
  - [14. Function Templates \& Class Templates](#14-function-templates--class-templates)
    - [Definition](#definition-8)
    - [Why?](#why-6)
    - [Complete Example](#complete-example-9)
  - [15. Operator Overloading](#15-operator-overloading)
    - [Definition](#definition-9)
    - [Why?](#why-7)
    - [Complete Example](#complete-example-10)
  - [16. Function Overloading vs Function Hiding](#16-function-overloading-vs-function-hiding)
    - [Definition](#definition-10)
    - [Why Important?](#why-important)
    - [Complete Example](#complete-example-11)
  - [17. Real-World Example Implementation of OOP in C++ Project](#17-real-world-example-implementation-of-oop-in-c-project)
    - [Concepts Shown](#concepts-shown)

---

## 1. Introduction to OOP

### What is OOP?
Object-Oriented Programming (OOP) is a programming paradigm that uses **objects** and **classes** to structure software. It models real-world entities and relationships, making programs more intuitive to design and maintain.

### Why do we use OOP?
- **Reusability** – Classes and objects can be reused in different programs or parts of the same program.  
- **Modularity** – The program is divided into smaller, more manageable pieces (classes and objects).  
- **Security** – Data can be protected using encapsulation and access specifiers.  
- **Maintainability** – Separating logic into classes makes debugging and updating easier.  
- **Scalability** – OOP designs handle complexity better as projects grow larger.

---

## 2. Access Specifiers in C++

### Definition
**Access specifiers** determine how the members (variables and functions) of a class can be accessed. They define the visibility and scope of class members.

### Why do we use Access Specifiers?
- **Encapsulation** – Keeps sensitive data hidden from unwanted direct access.  
- **Control** – Allows a class designer to decide which parts of a class are accessible from the outside.  
- **Clarity** – Makes it clear which methods are intended for public use and which are internal implementation details.

### Table of Access Specifiers

| Access Specifier | Accessible Within Class | Accessible in Derived Class | Accessible Outside Class |
|------------------|-------------------------|----------------------------|--------------------------|
| **private**      | Yes                     | No                         | No                       |
| **protected**    | Yes                     | Yes                        | No                       |
| **public**       | Yes                     | Yes                        | Yes                      |

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Example {
private:
    int privateVar;

protected:
    int protectedVar;

public:
    int publicVar;

    // Constructor
    Example() : privateVar(10), protectedVar(20), publicVar(30) {}

    void showValues() {
        cout << "Private: " << privateVar
             << ", Protected: " << protectedVar
             << ", Public: " << publicVar << endl;
    }
};

class Derived : public Example {
public:
    void showDerived() {
        // privateVar is not accessible here
        cout << "Protected in Derived: " << protectedVar
             << ", Public in Derived: " << publicVar << endl;
    }
};

int main() {
    Example obj;
    obj.showValues();

    // We can directly access publicVar
    cout << "obj.publicVar: " << obj.publicVar << endl;

    Derived d;
    d.showDerived();

    return 0;
}
```

---

## 3. Four Pillars of OOP

### 3.1 Encapsulation

**Definition**: Encapsulation is about bundling the data (attributes) and methods (functions) that operate on that data into a single unit (class). It also involves restricting access to the internal representation of the object.

**Why?**
- **Data Protection** – Prevents unintended access or modifications to the data.  
- **Cleaner Code** – Users of a class only interact with public methods. Implementation details remain hidden.  

**Complete Example**:

```cpp
#include <iostream>
using namespace std;

class BankAccount {
private:
    double balance;  // Encapsulated data

public:
    void setBalance(double b) {
        // Additional checks or validation can be done here
        balance = b;
    }

    double getBalance() {
        return balance;
    }
};

int main() {
    BankAccount account;
    account.setBalance(5000.0);
    cout << "Balance: " << account.getBalance() << endl;
    // Direct access to 'balance' is not allowed: account.balance = 10000.0; // Error
    return 0;
}
```

---

### 3.2 Abstraction

**Definition**: Abstraction means exposing only the essential details while hiding the complex internal implementation from the user.

**Why?**
- **Reduce Complexity** – Users of a class don’t need to know its complex internal details.  
- **Ease of Use** – Simplifies interaction; you only show what the user needs.  

**Complete Example**:

```cpp
#include <iostream>
using namespace std;

class ATM {
public:
    void withdrawMoney(double amount) {
        if (authenticateUser()) {
            if (processTransaction(amount)) {
                cout << "Transaction Successful. $" << amount << " Withdrawn.\n";
            } else {
                cout << "Transaction Failed.\n";
            }
        } else {
            cout << "Authentication Failed.\n";
        }
    }

private:
    bool authenticateUser() {
        // Complex user authentication logic
        cout << "Authenticating user...\n";
        return true; // Simplified for example
    }

    bool processTransaction(double amount) {
        // Complex transaction logic
        cout << "Processing transaction of $" << amount << "...\n";
        return true; // Simplified for example
    }
};

int main() {
    ATM atm;
    atm.withdrawMoney(100.0);
    return 0;
}
```

---

### 3.3 Inheritance

**Definition**: Inheritance allows a new class (derived/child) to acquire the properties and behaviors of an existing class (base/parent).

**Why?**
- **Code Reusability** – Avoids duplication of common methods and attributes.  
- **Hierarchy Representation** – Models real-world relationships in a layered approach (e.g., Animal → Dog).  
- **Easy Maintenance** – Changes in the base class automatically propagate to derived classes.  

#### Types of Inheritance

1. **Single Inheritance**: One derived class inherits from a single base class.  
2. **Multiple Inheritance**: A derived class inherits from more than one base class.  
3. **Multilevel Inheritance**: A class is derived from a derived class. (Grandparent → Parent → Child)  
4. **Hierarchical Inheritance**: Multiple derived classes inherit from a single base class.  
5. **Hybrid Inheritance**: A combination of two or more of the above forms.

**Complete Example (Multiple forms)**:

```cpp
#include <iostream>
using namespace std;

// Base class (Parent)
class Animal {
public:
    void eat() {
        cout << "Eating...\n";
    }
};

// Single Inheritance
class Dog : public Animal {
public:
    void bark() {
        cout << "Barking...\n";
    }
};

// Another base class
class Domestic {
public:
    void isPet() {
        cout << "I am a domestic pet!\n";
    }
};

// Multiple Inheritance (Dog inherits from Animal and Domestic)
class Labrador : public Animal, public Domestic {
public:
    void friendly() {
        cout << "I am a friendly Labrador.\n";
    }
};

// Multilevel Inheritance
class Puppy : public Dog {
public:
    void cute() {
        cout << "I am a cute puppy.\n";
    }
};

int main() {
    // Single Inheritance demonstration
    Dog dog;
    dog.eat();   // from Animal
    dog.bark();  // from Dog

    // Multiple Inheritance demonstration
    Labrador lab;
    lab.eat();    // from Animal
    lab.isPet();  // from Domestic
    lab.friendly();

    // Multilevel Inheritance demonstration
    Puppy pup;
    pup.eat();  // from Animal (inherited via Dog)
    pup.bark(); // from Dog
    pup.cute(); // from Puppy

    return 0;
}
```

---

### 3.4 Polymorphism

**Definition**: Polymorphism allows the same function name or operator to perform different behaviors.

**Why?**
- **Flexibility** – Single interface with multiple possible underlying implementations.  
- **Readability** – Reduces the number of function names needed.  

**Types**:
1. **Compile-time Polymorphism** (Function overloading, Operator overloading)  
2. **Run-time Polymorphism** (Virtual functions)

**Complete Example (Function Overloading)**:

```cpp
#include <iostream>
using namespace std;

class MathOperations {
public:
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
};

int main() {
    MathOperations math;
    cout << "add(int, int): " << math.add(3, 4) << endl;
    cout << "add(double, double): " << math.add(2.5, 1.7) << endl;
    return 0;
}
```

---

## 4. Constructor & Destructor Execution Flow

### Definition
- **Constructor**: A special member function that initializes objects of its class. Automatically called when an object is created.
- **Destructor**: A special member function that cleans up when an object goes out of scope or is deleted.

### Why use them?
- **Safe Initialization** – Ensures an object starts in a valid state.
- **Resource Management** – Ensures timely release of resources (e.g., memory, file handles).

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Test {
public:
    Test() {
        cout << "Constructor Called\n";
    }
    ~Test() {
        cout << "Destructor Called\n";
    }
};

int main() {
    cout << "Main Started\n";
    {
        Test t1;  // Constructor called here
    } // t1 goes out of scope, Destructor called here
    cout << "Main Ended\n";
    return 0;
}
```

**Possible Output**:
```
Main Started
Constructor Called
Destructor Called
Main Ended
```

---

## 5. Composition, Aggregation & Association

### Definitions

- **Association**: A relationship where two classes are connected but can exist independently.  
- **Aggregation** (weak ownership): A specialized form of Association where one class owns an object of another, but the owned object can outlive the owner.  
- **Composition** (strong ownership): A specialized form of Association where the lifetime of the owned object is dependent on the owner class.

### Why use them?
- To model real-world relationships between objects.
- To clarify ownership and lifetime responsibilities of objects.

### Table Representation

| Relationship   | Ownership        | Lifetime Dependency |
|----------------|------------------|---------------------|
| Association    | No direct owner  | Independent         |
| Aggregation    | Weak ownership   | Part can outlive whole |
| Composition    | Strong ownership | Part depends on whole |

### Complete Examples

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Composition Example
// Car "composes" an Engine - The Engine is created and destroyed with Car
class Engine {
public:
    Engine() { cout << "Engine created.\n"; }
    ~Engine() { cout << "Engine destroyed.\n"; }
};

class Car {
private:
    Engine engine; // Composition (engine's lifetime = car's lifetime)
public:
    Car() { cout << "Car created.\n"; }
    ~Car() { cout << "Car destroyed.\n"; }
};

// Aggregation Example
// Team has a list of Players, but Players can exist outside a Team
class Player {
public:
    string name;
    Player(const string& n) : name(n) {}
};

class Team {
private:
    vector<Player*> players; // Aggregation (pointers to existing Players)
public:
    void addPlayer(Player* p) { players.push_back(p); }
    void showPlayers() {
        for (auto p : players) {
            cout << p->name << " ";
        }
        cout << endl;
    }
};

// Association Example
// Teacher and Classroom are associated, but each can exist independently
class Classroom {
public:
    string roomNumber;
    Classroom(const string& room) : roomNumber(room) {}
};

class Teacher {
public:
    void teachesIn(Classroom& c) {
        cout << "Teacher teaches in room: " << c.roomNumber << endl;
    }
};

int main() {
    {
        cout << "=== Composition Demo ===\n";
        Car myCar;
    } // myCar goes out of scope, so does its Engine

    cout << "\n=== Aggregation Demo ===\n";
    Player p1("Alice"), p2("Bob");
    Team team;
    team.addPlayer(&p1);
    team.addPlayer(&p2);
    team.showPlayers(); // Team doesn't own players' lifetimes

    cout << "\n=== Association Demo ===\n";
    Teacher t;
    Classroom c("A101");
    t.teachesIn(c);

    return 0;
}
```

---

## 6. Shallow Copy vs Deep Copy

### Definition
- **Shallow Copy**: Copies the values of member variables **as is**, including pointers that end up sharing the same memory address.  
- **Deep Copy**: Allocates separate memory for pointer members, duplicating the pointed-to data instead of just copying the address.

### Why?
- **Avoid Shared Ownership Bugs** – Deep copies prevent accidental modification or deletion of shared memory.  
- **Ownership Clarity** – In shallow copy, multiple objects can refer to the same memory, complicating resource management.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class CopyDemo {
private:
    int* data;
public:
    // Constructor
    CopyDemo(int val) {
        data = new int(val);
        cout << "Constructor: allocated data with value " << *data << endl;
    }

    // Shallow Copy Constructor
    // CopyDemo(const CopyDemo& obj) {
    //     data = obj.data; // Shallow copy: both point to same address
    // }

    // Deep Copy Constructor
    CopyDemo(const CopyDemo& obj) {
        data = new int(*(obj.data)); // Deep copy: new memory allocated
        cout << "Deep Copy: allocated new data with value " << *data << endl;
    }

    // Destructor
    ~CopyDemo() {
        cout << "Destructor: freeing data with value " << *data << endl;
        delete data;
    }

    int getValue() { return *data; }
    void setValue(int val) { *data = val; }
};

int main() {
    CopyDemo obj1(10);
    CopyDemo obj2 = obj1;  // Calls deep copy constructor

    cout << "\nBefore changing obj1:\n";
    cout << "obj1: " << obj1.getValue() << ", obj2: " << obj2.getValue() << endl;

    obj1.setValue(20);

    cout << "\nAfter changing obj1:\n";
    cout << "obj1: " << obj1.getValue() << ", obj2: " << obj2.getValue() << endl;

    return 0;
}
```

---

## 7. Virtual Functions & Abstract Classes

### Virtual Functions

**Definition**: A function declared with the `virtual` keyword in a base class allows overriding in derived classes and enables **run-time polymorphism**.  

**Why?**  
- **Dynamic Binding** – The method called depends on the **actual object type**, not the pointer type.  
- **Flexibility** – Each derived class can provide its own specialized implementation.

**Complete Example**:

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() {
        cout << "Base show()\n";
    }
};

class Derived : public Base {
public:
    void show() override {
        cout << "Derived show()\n";
    }
};

int main() {
    Base* ptr = new Derived(); // Pointer of Base type, but object is Derived
    ptr->show();  // Calls Derived show() because of virtual
    delete ptr;
    return 0;
}
```

### Abstract Classes

**Definition**: A class is **abstract** if it has at least one **pure virtual function** (`virtual void func() = 0;`). Abstract classes **cannot** be instantiated directly.

**Why?**  
- **Blueprint** – Specifies an interface that derived classes must implement.  
- **Force Override** – Derived classes are forced to provide concrete implementations.

**Complete Example**:

```cpp
#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() = 0; // Pure virtual function -> Makes Shape an abstract class
};

class Circle : public Shape {
public:
    void draw() override {
        cout << "Drawing a circle.\n";
    }
};

class Rectangle : public Shape {
public:
    void draw() override {
        cout << "Drawing a rectangle.\n";
    }
};

int main() {
    // Shape s; // Error: cannot instantiate abstract class
    Shape* s1 = new Circle();
    Shape* s2 = new Rectangle();

    s1->draw();
    s2->draw();

    delete s1;
    delete s2;
    return 0;
}
```

---

## 8. Friend Function

### Definition
A **friend function** is a non-member function that has access to the private and protected members of a class.

### Why?
- **External Access** – Sometimes, external functions need to manipulate the internal state of a class.  
- **Operator Overloading** – Often used in operator overloading when both objects are on the right and left side of the operator.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Box {
private:
    int width;

public:
    Box(int w) : width(w) {}

    // Declare friend function
    friend void displayWidth(Box b);
};

// Friend function definition
void displayWidth(Box b) {
    // Can access private member
    cout << "Width: " << b.width << endl;
}

int main() {
    Box b1(10);
    displayWidth(b1); // Accesses private data
    return 0;
}
```

---

## 9. Static Members & Functions

### Definition
- **Static Members**: Shared by all objects of a class. They have **class scope**, not object scope.  
- **Static Functions**: Can be called **without** an instance of the class, and can only access static members.

### Why?
- **Shared Data** – Common data across all instances (e.g., counter of objects).  
- **Utility Functions** – Functions that do not require object-specific data.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Counter {
private:
    static int count; // Declaration of static variable

public:
    Counter() {
        count++;
    }
    static void showCount() {
        // Only static data can be accessed here
        cout << "Count: " << count << endl;
    }
};

// Definition of the static variable
int Counter::count = 0;

int main() {
    Counter c1, c2, c3;
    Counter::showCount(); // 3
    return 0;
}
```

---

## 10. This Pointer

### Definition
The **this** pointer is an implicit pointer available inside non-static member functions, pointing to the object that invoked the function.

### Why?
- **Disambiguate Member Names** – When parameter names and member names collide.  
- **Returning Reference** – Allows chaining calls by returning `*this`.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Person {
private:
    string name;

public:
    Person(string name) {
        // Use this-> to distinguish from constructor parameter
        this->name = name;
    }

    void display() {
        cout << "Name: " << this->name << endl;
    }
};

int main() {
    Person p("Alice");
    p.display();
    return 0;
}
```

---

## 11. V-Table & V-Table Pointer

### Definition
- **V-Table (Virtual Table)**: A table that holds pointers to the virtual functions of a class.  
- **VPTR (Virtual Pointer)**: A hidden pointer added by the compiler in an object that points to the class’s V-Table.

### Why?
- **Runtime Polymorphism** – The V-Table mechanism allows the program to dynamically bind function calls to the correct function implementation based on the actual object type.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    virtual void show() { cout << "Base show()" << endl; }
};

class Derived : public Base {
public:
    void show() override { cout << "Derived show()" << endl; }
};

int main() {
    Base* ptr = new Derived();
    ptr->show(); // Calls Derived's show() using V-Table
    delete ptr;
    return 0;
}
```

---

## 12. Diamond Problem & Virtual Base Class

### Definition: Diamond Problem
Occurs in **multiple inheritance** when a class (say `D`) inherits from two classes (`B` and `C`), which both inherit from the same base class `A`. This leads to **duplicate copies** of `A`.

### Why is it a Problem?
- **Ambiguity** – The compiler doesn’t know which copy of `A` to use when referencing members from `A`.  

### Virtual Base Class
Using **virtual** inheritance ensures only **one** shared base subobject.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class A {
public:
    int value;
    A() : value(100) {}
};

class B : virtual public A { };
class C : virtual public A { };

class D : public B, public C {
public:
    void showValue() {
        // No ambiguity with virtual base classes
        cout << "Value: " << value << endl;
    }
};

int main() {
    D obj;
    obj.showValue(); // Prints 100, only one A subobject exists
    return 0;
}
```

---

## 13. Dynamic Memory Allocation in OOP

### Definition
Allocating memory **at runtime** using operators `new` and `delete`.

### Why?
- **Control** – Create objects on the heap whose lifetime extends beyond the current scope.  
- **Flexibility** – Manage memory usage based on runtime conditions.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class DynamicClass {
private:
    int* data;

public:
    DynamicClass(int val) {
        data = new int(val);
        cout << "Constructor: Allocated memory.\n";
    }

    ~DynamicClass() {
        cout << "Destructor: Freed memory.\n";
        delete data;
    }

    void showData() {
        cout << "Data: " << *data << endl;
    }
};

int main() {
    DynamicClass* obj = new DynamicClass(42); // Allocated dynamically
    obj->showData();
    delete obj; // Must explicitly delete to call destructor
    return 0;
}
```

---

## 14. Function Templates & Class Templates

### Definition
Templates allow writing **generic** functions/classes that work with different data types without repeating code.

### Why?
- **Code Reuse** – A single function or class template can adapt to multiple types.  
- **Type Safety** – Compiler checks the correctness of template instantiations.

### Complete Example

**Function Template**:
```cpp
#include <iostream>
using namespace std;

template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << "add<int>(3, 4): " << add<int>(3, 4) << endl;
    cout << "add<double>(2.5, 1.5): " << add<double>(2.5, 1.5) << endl;
    return 0;
}
```

**Class Template**:
```cpp
#include <iostream>
using namespace std;

template <typename T>
class Storage {
private:
    T value;
public:
    Storage(T val) : value(val) {}
    T getValue() { return value; }
};

int main() {
    Storage<int> intStore(100);
    Storage<string> stringStore("Hello");

    cout << "intStore: " << intStore.getValue() << endl;
    cout << "stringStore: " << stringStore.getValue() << endl;
    return 0;
}
```

---

## 15. Operator Overloading

### Definition
**Operator Overloading** allows giving special meanings to **operators** (like `+`, `-`, `<<`, etc.) when applied to user-defined types (classes/structs).

### Why?
- **Natural Syntax** – Makes user-defined types as intuitive to use as built-in types.  
- **Readability** – Reduces need for verbose method calls.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Complex {
private:
    double real, imag;
public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    // Overload + operator
    Complex operator+(const Complex& c) {
        return Complex(real + c.real, imag + c.imag);
    }

    // Overload << operator for output
    friend ostream& operator<<(ostream& os, const Complex& c) {
        os << c.real << " + " << c.imag << "i";
        return os;
    }
};

int main() {
    Complex c1(1.5, 2.5), c2(2.0, 3.0);
    Complex c3 = c1 + c2; // Uses operator+(...)
    cout << "c1 + c2 = " << c3 << endl; // Uses operator<<
    return 0;
}
```

---

## 16. Function Overloading vs Function Hiding

### Definition

- **Function Overloading**: Same function name, different parameter lists (and/or types). Resolved at **compile time**.
- **Function Hiding**: A derived class function with the **same name** as a base class function **hides** the base class version, even if signatures differ.

### Why Important?
- Understanding the difference helps prevent unexpected hidden functions and clarifies how name lookups occur in inheritance hierarchies.

### Complete Example

```cpp
#include <iostream>
using namespace std;

class Base {
public:
    void show() { cout << "Base show()" << endl; }
};

class Derived : public Base {
public:
    // This hides Base::show() instead of overloading or overriding it
    void show(int x) { cout << "Derived show(int x): " << x << endl; }
};

int main() {
    Derived d;
    // d.show(); // Error: Base::show() is hidden, not accessible directly
    d.show(5);
    return 0;
}
```

> **Note**: If you want to use Base::show() in Derived, you might do `using Base::show;` inside Derived.

---

## 17. Real-World Example Implementation of OOP in C++ Project

Below is a simplified example combining multiple OOP concepts:  
- **Inheritance**, **Polymorphism** (virtual functions), **Encapsulation**, etc.

```cpp
#include <iostream>
#include <vector>
#include <memory>
using namespace std;

// Abstract Class
class Vehicle {
protected:
    string model;
public:
    Vehicle(const string& m) : model(m) {}
    virtual void startEngine() = 0;  // Pure virtual -> Abstract
    virtual ~Vehicle() {}
};

class Car : public Vehicle {
public:
    Car(const string& m) : Vehicle(m) {}
    void startEngine() override {
        cout << "Starting car engine for model: " << model << endl;
    }
};

class Bike : public Vehicle {
public:
    Bike(const string& m) : Vehicle(m) {}
    void startEngine() override {
        cout << "Starting bike engine for model: " << model << endl;
    }
};

int main() {
    // Polymorphic behavior using base class pointers
    vector<unique_ptr<Vehicle>> vehicles;
    vehicles.push_back(make_unique<Car>("Toyota"));
    vehicles.push_back(make_unique<Bike>("Yamaha"));

    for (auto& v : vehicles) {
        v->startEngine(); // Calls the appropriate override
    }
    return 0;
}
```

### Concepts Shown
- **Abstract Class** (`Vehicle`)  
- **Pure Virtual Function** (`startEngine() = 0`)  
- **Derived Classes** (`Car`, `Bike`)  
- **Polymorphism** (calling `v->startEngine()` resolves to `Car` or `Bike` at runtime)  
- **Encapsulation** (members hidden, only exposed methods used)  

---