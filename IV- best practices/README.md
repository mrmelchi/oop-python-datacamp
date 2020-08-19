# Best Practices

Polymorphism means using a unified interface to operate on objects of different classes.

## Cirlce Ellipse Problem

The classic example of a problem that violates the *Liskov Substitution* Principle is the **Circle-Ellipse problem**, sometimes called the **Square-Rectangle problem**.

By all means, it seems like you should be able to define a class **Rectangle**, with attributes h and w (for height and width), and then define a class **Square** that inherits from the Rectangle. After all, a square "is-a" rectangle!

- Create a class Rectangle with a constructor that accepts two parameters, h and w, and sets its h and w attributes to the values of h and w.
- Create a class Square inherited from Rectangle with a constructor that accepts one parameter w, and sets both the h and w attributes to the value of w.

## Managing Data Access

All class data in Python is technically public. The fundamental behind much of Python design, "We are all adults here". It's a philosophy that goes beyond just code and describes how the Python community interacts with each other. But there are some few ways to manage acces to data.

- **Naming Conventions:** The first and most important convention is using a single leading underscore (`_name`) to indicate a method or, attribute which isn't the part of a public interface and can change without notice. Though nothing is restricting to modify this attributes or, methods technically. But sometimes, class developer includes something like "Do not touch this" believing that the users will be using it responsibly. Class developers use it for implementation details or, helper functions.
  - **pseduoprivate attributes:** Attributes and methods whose name starts with double underscroe are the closest thing to "private" fields/methods. This data is not inherited. Python performs *Name mangling* where `obj.__attr_name` is interpreted as `obj._MyClass__attr_name`.

- **Properties for customized access:**
  - Properties are special becuase the user of the class won't have to do anything special because they behave like properties. Developer have some control over the access.
  - Use *protected* attribute with leading _ to store the data.
  - Use a decorator `@property` on a method whose name is exactly the name of the restricted attribute and return the initial attribute.
  - Use `@attribute_name.setter` on a method `attribute_name()` which will be called on `obj.attribute_name = value`. We can validate and set the attribute in this case.
  - If the `@attribute_name.setter` then the property will be `read-only` like `DataFrame.shape`.
  - To retrieve a property's value we use `@attribute_name.getter` and when the property is deleted use `@attribute_name.deleter`

    ```python
    class Employer:
        def __init__(self, name, new_salary):
            self._salary = new_salary

        @property
        def salary(self):
            return self._salary

        @salary.setter
        def salary(self, new_salary):
            if new_salary < 0:
                raise ValueError("Invalid salary")
            else:
                self._salary = new_salary
    ```
