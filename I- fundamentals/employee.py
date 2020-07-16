class Employee(object):
    '''
    Class representing a company employee.
    
    Attributes
    ----------
    name : str 
        Employee's name        
    email : str, default None
        Employee's email
    salary : float, default None
        Employee's salary
    rank : int, default 5
        The rank of the employee in the company hierarchy (1 -- CEO, 2 -- direct reports of CEO, 3 -- direct reports of direct reports of CEO etc). Cannot be None if the employee is current.
    '''
    def __init__(self, name, email=None, salary=None, rank=5):
        '''
        Create an Employee object
        '''
        self.name = name
        self.email = email

        if salary >= 0:
            self.salary = salary
        else:
            self.salary = 0
            print('Invalid salary!')
        
        self.rank = rank
    
    def give_raise(self, amount):
        '''
        Raise employee's salary by a certain `amount`. Can only be used with current employees.

        Example usage:
            # emp is an Employee object
            emp.give_raise(1000)
        '''
        if amount > 0: 
            self.salary += amount

    def promote(self):
        '''
        Promote an employee to the next level of the company hierarchy. Decreases the rank of the employee by 1. Can only be used on current employeed who are not at the top of the hierarchy.
        
        Example usage:
            # emp is an Employee object
            emp.promote()
        '''
        self.rank += 1



if __name__ == "__main__":
    employee = Employee(name='Shunjid', email='s@s.com', salary=73500, rank=2)
    print('previous salary : {}'.format(employee.salary))

    employee.give_raise(1000.0)
    print('current salary  : {}'.format(employee.salary))