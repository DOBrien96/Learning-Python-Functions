letters = ["a", "b", "c"]
matrix = [[0,1], [2,3]]
zeros = [0] * 100
list(range(20))
chars = list("Hello World")

#The letters dictionary is a dynamic list meaning it can have it's values changed
#where as the matrix dixtionary is called a matrix because it's 2 dimentional
#Line 3 is a simple way to repeat 100 zeros, line 4 is a simple way of
#writing out alot of numbers efficiently. Line 5 uses the list function
#to print out each charater individualy.

letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])
print(letters[::2])
print(letters[::-1])

#Line 14 is how you call an index and then change it to "A". Line 15 is 
#a means of calling a range within the index, if you leave the first and
#second value empty it will assume the first index value (0) and the last
#index value respectively . Line 16 with the "::" function is telling to skip
#each increment until completion, that means line 16 will skip every other
#index, so it should print "a" & "c". Line 17 allows you to do everything
#like line 16 but from the back instead.

numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *others, last = numbers
print(first, last)
print(others)

#When calling a list the word "first" and "last" act as a function as well as
#a variable and do what they say, the "*" calls all other non called values
#in the list.

letters = ["a", "b", "c"]

for index, letter in enumerate(letters):
    print(index, letter)
    
#The index variable acts as a funtion which will cal the index of each letter
#we also assign the dictionary letters with a new variable called letter

letters = ["a", "b", "c"]

letters.append("d")
letters.insert(4, "e")

#append function adds at the end of a list
#insert function allows you to insert where ever you want in the list,
#the first value is the index of where you want to store the second value

letters.pop()
letters.remove("b")
del letters[0:3]
letter.clear()
letter.count()

#the pop function removes the last value within the list, however, you can 
#choose a diferent value to remove by specifying it's index in the parenthesis
#.remove is the same as pop but you get to remove an index by it's value and
#not it's index number. the del function gives you the option of choosing a
#range within the list and .clear clears the whole list, the count function
#gives you the ability to count how many of specific value is in a list, or
#if you leave the parenthesis empty it will tell you the max index

numbers = [3, 51, 2, 8, 6]

numbers.sort()
sorted(numbers)

#The sort function will fix the list and re-arrange the list in order. The 
#sorted function will not change the original list unlike the sort function
#and will provide you with the same results

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
    
prices = list(map(lambda item: item[1], items))
print(prices)

#The labmda function is an undefined funtion (meaning you can define it)
#that can have as many arguments as you want but only one expression,
#lambda funtions are also useful when you want to use the function once.
#Line 82 uses the map function to order the list by the value of 
#Products (10, 9, 12) and not by name, but in order to tell map what to
#order you will need to call the annonymose function lambda and specify 
#somethings. The item argument is the new variable for the items list 
#name, item[1] is specifying which column you want to order the list by,
#the "list()" function will then create a new list and store the results 
#on that new list.

#Here is a simplified version of a newly defined lambda function that we
#will only need once.

# declare a lambda function
greet = lambda : print('Hello World')
# call lambda function
greet()
# Output: Hello World

filtered = list(filter(lambda item: item[1] >= 10, items))

#Line 105 filters out any products below 10

prices = [item[1] for item in items]

filtered = [item for item in items if item[1] >= 10]

#Line 109 is called a list comprehension and is a shorter, cleaner and
#more performant than version of line 82, line 111 is the same principle
#for line 105

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

#The zip() function allows you to combine lists, you use the list() 
#function to store the reuslts into a newly generated list, by adding
#the abc string, the code will print like so a,1,10 , b,2,20 , c,3,30

browsing_session = []
browsing_session.append(1)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]
    
#From lines 126 to 130 this is called LIFO method, LIFO stands for
#last in first out, it means what it says, last piece of data in so 
#the newest data in that list, is the first piece of data to go out 
#if popped or pop(), the opposite of this is FIFO - first in first out
#you can use a function call popleft() from the collections
#module to implement fifo 

tuple = (1, 2)

#A tuple is an unchangeable list

tuple = tuple("Hello World")

#This tuple fnction will convert each character in the string too a
#tuple of 11 strings meaning each character becomes it's own string

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second) #The | symbol combines all the numbers from both lists but doesn't print duplicates
print(first & second) #The & symbol combines the lists and only prints duplicate results
print(first - second) #The - symbol removes matching values from the first list and prints what's left
print(first ^ second) #The ^ symbol will return any values that are not in both lists


