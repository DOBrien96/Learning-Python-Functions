from sys import getsizeof

point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

#Both are the exact same but line 2 is a more efficient way of inputing
#data because you dont have to type quotes

point["x"]

#Unlike lists, dictionaries dont operate using index, so you have to
#call the string in order to find data in a dictionary

if "a" in point:
    print(point["a"])
print(point.get("a", 0))

#This is an algorithm that sets a to 0 if it doesn't already exist in
#the dictionary

del point["x"]

#This is the basic delete function for dictionaries

for key, value in point.items():
    print(key, value)

#This will print everything with its value.

values = []
for x in range[5]:
    values.append(x * 2)
    

values = [x * 2 for x in range(5)] # List

values = {x * 2 for x in range(5)} # Set

values = {x: x * 2 for x in range(5)} # Dictionary


#Line 28 - 30 & 33 are the same but 33 is less noisy, line 33 is called
#line comprhension and can be used for sets (replace "[]" for "{}"),
#lists and dictionaries 

values = (x * 2 for x in range(10000)) # Tuple
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

#Line 46 is called a generator expression instead of a dictionary
#comprehension because it doesnt store all the data in memory like a
#list, this is helpful for when you're dealing with a large data set
#or an infinite amount of data. The downside of generator expressions
#is you won't be able to call the total amount of data as it wont be stored

numbers = [1, 2, 3]
print(*numbers)

#Line 58 is unpacking the dictionary meaning thier will be no brackets
#when you print it like it would be if you where to type print(numbers),
#the astric (*) is the unpacking operator

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

#This is another example of unpacking but with a string instead.

first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}

#You use two ** to unpack a dictionary, one thing to note is if a key
#is the same in both lists the last value to be called upon is what the
#key is now set too.