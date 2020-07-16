# Fundamentals

## When do we need procedural programming

- When we need to code as a sequence of steps.
- Appropiate during data analysis:
  - Download the data
  - Process the data
  - Visualize

## When do we need OOP

When our application uses more data and it has a vast amount of functionalities the harder it is think it to be a sequence of steps. Instead, we manipulate it as a collection of objects and patterns of their interactions. For example: **users** interacting with elements of an interface.

- Code as interaction of objects
- Great for building frameworks, GUI, API or, building tools like pandas dataframes
- Organied maintainable & reusable code

## Objects as data structure

An object is a data structure incorporating information about state and behaviour. One of the special features of OOP is that the states and behaviours are bundled together. For example: Intead of thinking 'Customer' data seperate from 'Customer' actions, we think of them as one unit representing a customer. This is called **Encapsulation**.

The real strength of OOP comes from utilizing classes. Classes are like blueprints for objects. The describe the possible states & behaviours that every object of a certain type could have. By defining a class you just describe something in a unified way. Then the specific objects are just the realization of that class with their particular states & behaviours.

## Attributes and Methods

State information are stored in Attributes & behaviour information are stored in methods. Attributes are represented by variables & methods are repsented by functions both are accessible by the dot(.) syntax of an object. Examples:

```python
import numpy as np

a = np.array([1, 2, 3, 4])

# shape is an attribute of numpy
np.shape
```

```python
import numpy as np

a = np.array([1, 2, 3, 4])

# reshape is a method of numpy
np.reshape(2, 2)
```

To list all the attributes and methods of an object use 'dir' on it.

```python
dir(a)
```
