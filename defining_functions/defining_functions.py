def greet():
    print("Hi there!")
    print("Welcome aboard")
    
    
greet()

#This is called defining a function, the "greet()" is a function with other
#functions inside of it which will be called upon when you call the greet()
#function on line 6.

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
    
    
greet("Dylan", "O'Brien")


#When defining a function you can input something called arguments in the 
#parenthesis, note that you don't call them parameters because it's a 
#defined function, when you input these arguments you have to assign
#them a value otherwise you will recieve an error

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Dylan")

print(message)

#Line 25 & 26 are a improved version of lines 12 to 17 because you
#can reuse lines 25 and 26 for other things within your code unlike lines
#between 12 to 17 which are now permanently assigned to printing in the terminal

def increment(number, by):
    return number + by


print(increment(2, by=1))

#On line 41 you can see I have put by=1, although this is not necessary
#it helps make code far mor easier to read, this is called a keyword argument
#and should be a standard when writhing code. You can give arguments a default
#value and not even need to type out by=1 on line 41 by putting by=1 on 
#line 37.

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

#By using "*" on line 49 you can call multiple values in a single argument
#As you can see this is helpful for things such as multiplying multiple 
#numbers. You call the "*" an xargs when used this way within a defined argument.
#xargs is x = multiple, args = argument creates the word "xargs".

def save_user(**user):
    print(user["name"])
    
    
save_user(id=1, name ="John", age=22)

#Using the "**" function on line 63 stores all the data you give the function into the 
#"save_user" into a callable dictionary argument which I have called user,
#on line 64 by changing the key in "[]" I can now print the value of the key.
#This is called an xxargs