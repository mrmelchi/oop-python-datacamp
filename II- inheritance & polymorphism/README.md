# Inheritance and Polymorphism

## Distinguish: Instance level data & Class level data

In this code below, we can assign specific values to the attibutes name and salary for each new instance of the class. These attributes are called **instance attributes**. We use self to bind them to a particular instance.

```python
class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee('John', 80000)
emp2 = Employee('Doe', 20000)
```

But what if we needed to store some data which can be shared among all instances of a class? For example, introducing a minimal salary accross the organization. That data should not differ among object instances. In such case, we can directly define the attribute in the class body. These attributes are called **class attributes** which will serve as a global variable within the class. We can use this attribute inside the class like we would use any global variable only prepended by the class name.

```python
class Employee(object):
    # Class attribute
    MIN_SALARY = 30000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary if salary >= Employee.MIN_SALARY else self.salary = Employee.MIN_SALARY
```

### Why should we use class attributes

- Defining global constants which are related to the class.
- Minimum/Maximum values for attributes.
- Commonly used values and constants like `PI = 3.1416` in a `Circle` class.

## Class methods

Regular methods are already shared between instances. The same code gets executed for every instance. The only difference is the data that is fed into it. It is possible to define methods bound to class rather than an instance. But they have a narrow application scope like they can't use any instance level data. We use `@classmethod` decorator to define a class method followed by a method description.

```python
class A:
    @classmethod
    def sum(cls, args...):
        # Do something

# Calling a class method
A.sum(args...)
```

The only difference is that the first argument is not self but cls which is refering to the class just like self argument is a reference to a particular instance.

### Why should we use class methods

Using as an alternative constructor. For example, instead of creating an object by passing values through it's instance we might want to instantiate a class from a file data. For example:

```python
@classmethod
def from_file(cls, file_name):
    # Read from file
    with open(file_name, 'r') as f:
        name = f.readline()
    # cls(..) will call __init__(...)
    return cls(name)
```
