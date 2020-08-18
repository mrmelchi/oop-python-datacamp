# Standard Python

```python
class Customer:
    def __init__(self, name, balance):
        self.name, self.balance = name, balance


customer1 = Customer('John', 3000)
customer2 = Customer('John', 3000)
```

Let's say we have two objects of Customer class with same data. If we ask python the objects are equal or, not `customer1 == customer2` the answer will be `False`. By default, Python doesn't consider two objects to be same because they are stored in different chunks of memory.

When an object is created, Python allocates a chunk of memory to that object and the variable that the object is assigned to actually contains just the reference of the memory chunk. For example: `0x1f8598e2e48`. In the last 2 instuctions of above code we are just telling Python to allocate a chunk of memory for Customer object and label it as customer1, same goes for customer2.

> So, when we are comparing customer1 and customer2 we are actually comparing the references not the data.

But it doesn't have to be always that way. We know, numpy arrays can be compared using their data. For example:

```python
import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 3])

array1 == array2
```

> So, how can we enforce this for our custom classes?

Whenever two objects of a same class are compared, Python by default call the `__eq__` method. We can redefine this method to perform custom comparison code. Other comparison:

| Operator | Method |
| ------------- | ------------- |
| ==       | _\_eq__() |
| !=       | _\_nq__() |
| >=       | _\_gq__() |
| <=       | _\_lq__() |
| >        | _\_gt__() |
| <        | _\_lt__() |

There is a `__hash__()` method that allows us to use objects as dictionary keys and in sets.

## String representation

There are two special methods that we can define in a class that will return a printable representation of an object.

- `__str__()` - Suppossed to give informal representation, suitable for end-user
- `__repr__()`- Formal. Mainly used by developers. Mostly preferred because it reproduces representation and a fallback for print when str isn't defined.
