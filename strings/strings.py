course = "Python Programming"

message = """
Hi Learner,

This triple quotes are useful to format large forms of text
like an email.


Sincerly,
        Dylan

"""

print(message)

#The len function allows you to print how many characters 
#are in the string

print(len(course))

#You can use [] to print a specific part of a string,
#the starting number is 0 not 1 and if you input -1 
#it will start from the end of the string.

print(course[0:6])

print(course[-1])

#You're also able to start from a diferent number like 7
#instead of 0, you also apply this too the end index too.

print(course[7:18])

#You can use the escape method "\" to avoid syntax errors,
#this is helpful for strings when maintaing grammer is important

escape = 'I\'m getting out of here'

#\n creates a new line

new_line = "\n These \n are \n new \n lines."

print(escape, new_line)

#You can use "f" to format strings, this allows you to add spaces
#without having to type of a string.
#To add variables to your formatted string use the "{}" syntax

first = "Dylan"
last = "O\'Brien"
full_name = f"{first} {last}"

print(full_name)

#You can call functions for you variables by useing the "." syntax
#I'm going to uppercase my full name using the upper function

print(full_name.upper())

#You can ask for a boolean method in a string by typing

print("Dylan" in full_name)