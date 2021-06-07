# Object Oriented Programming for C++

[W3 Schools](https://www.w3schools.com/cpp/cpp_oop.asp)

OOP stands for Object-Oriented Programming.

Procedural programming is about writing procedures or fuctions that perform operations on the the data, while object-oriented programming is about creating objects that contain both data and functions.

## Directory

* 

## Advantages of OOP

* faster and easy to execute
* clear structure for programs
* DRY "don't repeat yourself", easier to maintain, modify, and debug
* create reusable applications with less code and shorter development time

### DRY

The principle is about reducing the repetition of code. You can extract code that are common for the app, and then place it in a single place and reuse instead of repeating.

## Classes and Objects

Classes and objects are the two main aspects of object-oriented programming. Here are some common examples used.

| Class | Object |
|:-:|:-:|
| Fruit | Apple, Banana, Mango |

Another example:

| Class | Object |
|:-:|:-:|
| Car | Volvo, Audi, Toyota |

A class is a template for objects and an object is an instance of a class. When the individual object is created, it inherits all the variables and functions from the class.

### Example of a Class

```cpp
class MyClass {       // The class
  public:             // Access specifier
    int myNum;        // Attribute (int variable)
    string myString;  // Attribute (string variable)
};
```

#### Keywords

* __class__ keyword is used to create a class called MyClass
* __public__ keyword is an __access specifier__, which specifies that members (attributes and methods) of the class are accessible from outside the class.
* inside of the class, there is an integer variable and a string variable
* finally, end the class definitino with a semicolon __;__

###

---

## Create an Object

In C++, an object is created from a class, and since we've just created a class, we can use it to create an object.

```cpp
int main() {
  MyClass myObj;  // Create an object of MyClass

  // Access attributes and set values
  myObj.myNum = 15; 
  myObj.myString = "Some text";

  // Print attribute values
  cout << myObj.myNum << "\n";
  cout << myObj.myString;
  return 0;
}
```
