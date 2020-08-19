# Best Practices

Polymorphism means using a unified interface to operate on objects of different classes.

## Cirlce Ellipse Problem

The classic example of a problem that violates the *Liskov Substitution* Principle is the **Circle-Ellipse problem**, sometimes called the **Square-Rectangle problem**.

By all means, it seems like you should be able to define a class **Rectangle**, with attributes h and w (for height and width), and then define a class **Square** that inherits from the Rectangle. After all, a square "is-a" rectangle!

- Create a class Rectangle with a constructor that accepts two parameters, h and w, and sets its h and w attributes to the values of h and w.
- Create a class Square inherited from Rectangle with a constructor that accepts one parameter w, and sets both the h and w attributes to the value of w.
