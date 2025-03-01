Here is the properly formatted **Markdown (`.md`) file** version of your **SOLID Principles in C++** document:

```md
# **SOLID Principles in C++**

The **SOLID** principles are five key design principles in object-oriented programming that help developers create more **maintainable, scalable, and flexible** code.

---

## **1. Single Responsibility Principle (SRP)**

### **Complete Definition:**
A class should have **only one reason to change**, meaning it should have **only one job or responsibility**. This reduces coupling and makes the system easier to maintain.

### **Simple Explanation:**
A class should **do only one thing** and should have **one reason to change**.

### **Easy Way to Remember:**
Think of a **worker in a restaurant**:
- A **chef** cooks food.
- A **waiter** serves food.
- A **cashier** handles payments.
- If one person did all these jobs, changing the menu, service, or payment method would affect everything.
- Instead, each person has **one responsibility** to keep things manageable.

### **Example Scenario:**
A system that generates a report and saves it to a file.

### **Bad Example (Violating SRP)**
```cpp
#include <iostream>
#include <fstream>
using namespace std;

class Report {
public:
    void generateReport() {
        cout << "Generating report..." << endl;
    }

    void saveToFile(string filename) {
        ofstream file(filename);
        file << "Report data" << endl;
        file.close();
    }
};

int main() {
    Report report;
    report.generateReport();
    report.saveToFile("report.txt"); // ❌ Violates SRP
    return 0;
}
```
**❌ Problem:** The `Report` class is handling **both** generating and saving reports.

### **Good Example (Following SRP)**
```cpp
class Report {
public:
    void generateReport() {
        cout << "Generating report..." << endl;
    }
};

class ReportSaver {
public:
    void saveToFile(string filename) {
        ofstream file(filename);
        file << "Report data" << endl;
        file.close();
    }
};

int main() {
    Report report;
    ReportSaver saver;

    report.generateReport();
    saver.saveToFile("report.txt"); // ✅ Follows SRP
    return 0;
}
```
✅ **Solution:** We separate **report generation** and **report saving** into different classes.

---

## **2. Open/Closed Principle (OCP)**

### **Complete Definition:**
A class should be **open for extension but closed for modification**. This means that new functionality should be added **without modifying existing code**.

### **Simple Explanation:**
You should **extend a class** rather than **modifying it** when new features are needed.

### **Easy Way to Remember:**
Imagine a **mobile app** that allows users to **log in with email**. If we later want to add **Google and Facebook login**, we should **extend** the functionality rather than modifying the existing login code.

### **Bad Example (Violating OCP)**
```cpp
class AreaCalculator {
public:
    double calculateArea(string shape, double radius = 0, double length = 0, double breadth = 0) {
        if (shape == "circle") {
            return 3.14 * radius * radius;
        } else if (shape == "rectangle") {
            return length * breadth;
        }
        return 0;
    }
};

int main() {
    AreaCalculator calc;
    cout << "Circle area: " << calc.calculateArea("circle", 5) << endl; // ❌ Violates OCP
    return 0;
}
```
**❌ Problem:** If we want to add a new shape, we must modify the class.

### **Good Example (Following OCP)**
#### **Without Pointers**
```cpp
class Shape {
public:
    virtual double getArea() = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
    double radius;
public:
    Circle(double r) : radius(r) {}
    double getArea() override {
        return 3.14 * radius * radius;
    }
};

class Rectangle : public Shape {
    double length, breadth;
public:
    Rectangle(double l, double b) : length(l), breadth(b) {}
    double getArea() override {
        return length * breadth;
    }
};

int main() {
    Circle circle(5);
    Rectangle rectangle(4, 6);

    cout << "Circle area: " << circle.getArea() << endl; // ✅ Follows OCP
    cout << "Rectangle area: " << rectangle.getArea() << endl;

    return 0;
}
```
✅ **Solution:** Now, we can **add more shapes without modifying existing code**.

---

## **3. Liskov Substitution Principle (LSP)**

### **Complete Definition:**
A subclass should be able to replace its parent class **without altering the correctness of the program**. Any child class must adhere to the expected behavior of its parent class.

### **Simple Explanation:**
A subclass should be a true extension of its parent class, and it should not change the behavior that the parent class guarantees.

### **Easy Way to Remember:**
Imagine you have a **universal remote** that works with all TVs. If you replace the remote with a new one, it should still work with all TVs.

### **Good Example (Following LSP)**
```cpp
class SmartRemote : public RemoteControl {
public:
    void turnOnTV() {
        cout << "Turning on Smart TV with voice control" << endl;
    }
};

int main() {
    SmartRemote remote;
    remote.turnOnTV(); // ✅ Correctly follows LSP
    return 0;
}
```
✅ **Solution:** The `SmartRemote` can replace `RemoteControl` without breaking functionality.

### **Suggested Additions with Examples:**

#### **Liskov Substitution Principle (LSP) Violation Example**
```cpp
class Bird {
public:
    virtual void fly() {
        cout << "Bird is flying" << endl;
    }
};

class Ostrich : public Bird {
public:
    void fly() override {
        throw logic_error("Ostriches cannot fly!"); // ❌ Violates LSP
    }
};

int main() {
    Bird* b = new Ostrich();
    b->fly(); // ❌ Throws an error, breaking expectations
    delete b;
    return 0;
}
```
✅ **Fix:** Introduce a base class with the correct abstraction:
```cpp
class Bird {
public:
    virtual void makeSound() = 0;
};

class FlyingBird : public Bird {
public:
    virtual void fly() = 0;
};

class Sparrow : public FlyingBird {
public:
    void fly() override {
        cout << "Sparrow is flying" << endl;
    }
    void makeSound() override {
        cout << "Chirp Chirp" << endl;
    }
};

class Ostrich : public Bird { // Now, Ostrich does NOT inherit fly()
public:
    void makeSound() override {
        cout << "Boom Boom" << endl;
    }
};
```

---

## **4. Interface Segregation Principle (ISP)**

### **Complete Definition:**
A class should not be forced to implement methods it does not use.

### **Simple Explanation:**
Instead of having one large interface, create smaller, more specific interfaces.

### **Easy Way to Remember:**
Imagine a printer:
- A **simple printer** only prints.
- A **multifunction printer** prints, scans, and copies.
- A **basic printer** should not be forced to implement `scan()`.

### **Bad Example (Violating ISP)**
```cpp
class Printer {
public:
    virtual void print() = 0;
    virtual void scan() = 0; // ❌ Not all printers scan
};
```

### **Good Example (Following ISP)**
```cpp
class Printable {
public:
    virtual void print() = 0;
};

class Scannable {
public:
    virtual void scan() = 0;
};
```
✅ **Solution:** Separate interfaces allow different types of printers.

---

## **5. Dependency Inversion Principle (DIP)**

### **Complete Definition:**
High-level modules should not depend on low-level modules. Both should depend on abstractions.

### **Simple Explanation:**
Instead of direct dependencies, use abstractions.

### **Easy Way to Remember:**
Think of a **USB port**:
- Instead of designing a computer to only work with `WiredKeyboards`, we make it work with any `Keyboard`.

### **Bad Example (Violating DIP)**
```cpp
class WiredKeyboard {
public:
    void connect() {
        cout << "Keyboard connected via wire" << endl;
    }
};
```

### **Good Example (Following DIP)**
```cpp
class Keyboard {
public:
    virtual void connect() = 0;
};
```
✅ **Solution:** Computer depends on an abstract `Keyboard`, making it flexible.

---