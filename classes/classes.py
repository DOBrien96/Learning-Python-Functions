

class Point:
    def draw(self):
        print("draw")
        
point = Point()
print(type(point))
print(isinstance(point, int))

#the instance function asks the variable "point" if it's an integer, you
#can change "int" to anything you want to ask the program, to see if it 
#belongs to the variable


class Case:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        

case = Case(1, 2)
case.draw()

    
#This __init__ function is a method we call a magic method or a 
#constructor. All the methods we define in a class should have at
#least one attribute which we call "self" by convention, self is a 
#reference to the current object. Using self we can read the current
#attributes of the object or we can also call other methods of this
#object.
#When calling methods of an object we never have to supply a value for 
#the parameter as python inteperator does that for us

case.z = 10

#Class attributes are dynamic, meaning you can add more to your class,
#The current attrributes are called instance attributes, well why are they
#call that? Instance attributes are what we've seen before. These are the 
#attributes that are independent to each object, like the door color 
#or the height of the door.


class Example:
    @classmethod
    def zero(cls):
        return cls(0, 0)


#Instance method are methods which require an object of its class to be 
#created before it can be called. To invoke a instance method, we have 
#to create an Object of the class in which the method is defined. cls
#is invoked as a argument to the class itself and you use the @classmethod
#to extend the behaviour of a method or function.

class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()

#Here is another exaple of a classmethod


class Numberz:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x == other.x and self.y == other.y
    

numberz = Numberz(10, 20)
other = Numberz(1, 2)

#Using the __str__ magic method function we're able to convert the results 
#of line 75/6 to a formatted string. The other two magic methods allow
#you to compare the objects without ruturning False because the two objects
#are always difrent in memory unless you tell it to compare the values.

class TagCloud:
    def __init__(self):
        self.__tags = {} #setting the "tags" attribute to a dictionary
    
    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1 
    
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
        
    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)
    

cloud = TagCloud()
cloud.add["python"]
cloud.add("python")
cloud.add("python")

#Line 101, this adds the string to the dictionary and puts a counter next 
#to it. "tag" represents the key we want to add so that is "python" in this
#case. When you add two underlines to an attribute like we have done to
#"__tags" above you make it private from outside the class and more difficult
#to access, this is handy when you don't want other users to access this
#attribute.

print(cloud.__dict__)

#when this is printed you can use the awnser of the print to access the dictionary

print(cloud.TagCloud__tags)

#This will return the results of the dictionary

class Product:
    def __init__(self, price):
        self.price = price
        
    @property
    def price(self):
        return self.__price
        
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value
        

product = Product(10)
print(product.price)
        
#line 140 applies an @property decorator/magic function to the object 
#so we can give the object an ideal name instead of a name with loads of 
#underlines and words, which makes the code more readable. Line 144 sets 
#the attribute for the object below as price has been used twice and not 
#giving the second object an attribute would crash the program.

isinstance() 

#This function allows you to see if a variable has a object class assigned
#to it, and will return a boolean value.

class Person:
    def greet(self):
        print("Person Greet")


class Manager(Person):
    pass


manager = Manager
manager.greet()

#When adding inheritence to a class the first class inherited will always
#dominate over the other classes and it goes from left to right, unless
#the class already has a method inside then the inherited classes are ignored


