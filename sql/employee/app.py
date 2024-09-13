class Employee:
    def __init__(self, first_name, last_name, age, salary):
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
        self.salary = salary 

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def __repr__(self):
        return "Employee('{}', '{}', {}, {})".format(self.first_name, self.last_name, self.age, self.salary)
    