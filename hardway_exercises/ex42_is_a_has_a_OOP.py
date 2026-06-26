##Animal is a object (yes, sort of comfusing) look at the extra credit
class Animal(object):
    pass

class Dog(Animal):

    def __init__(self, name): #
        self.name = name
   # Init will usuall have the data(attrs)
   # Methods / functions with self will work on the data (attrs) 
    def print_name(self):
        print(f"The dog name is {self.name}")


class Cat(Animal):
    def __init__(self, name):
        self.name = name

class Person(object):
    def __init__(self, name, pet):
        self.name = name
        ##person has a pet of some kind
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary, pet):
        super(Employee, self).__init__(name, pet)
        self.salary = salary


class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

##Rover is a dog
rover = Dog("Rover")
rover.print_name()


satan = Cat("Satan")
print(satan.name)

# mary = Person("Mary")

# mary.pet = satan

frank = Employee("Frank", 120000, "Mukku")
frank.pet = rover

flipper = Fish()
crouse = Salmon()
harry = Halibut()

emp1 = Employee("emp1", 10000, "Tommy")
print(emp1.pet)
p2 = Person("p2", "Moti")

emp2 = Employee(p2, 15000, "Rocky")

#few exmp for basics for object oriented programming for practise