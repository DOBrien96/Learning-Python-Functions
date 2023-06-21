try:
    with open("app.py") as file:#, open("another_file.txt") as example
        print("File opened.")
    age = int(input("Age: "))
    xfactor = 10 /age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown.")
#finally:
#   file.close()

#In this program we're looking to see if the user has input a valid
#value, in this case a number, and if they haven't then line 5 will
#tell the user they have input the wrong value and continue to run
#the program instead of crashing because theirs an error. To specify
#multiple errors use parenthesis and a comma like on line 5.
#The function on line 10 will run even when an exception is triggered 
#with a loop, but, a better way to make sure a file closes after we use
#it, is to use the with function, the with function will ensure any
#external resources you use is closed after you've used it, making
#line 10 - 11 redundant.

#Try not to use exceptions where you can as it has a perfomance cost
#when you want to scale up an app, try to use if statements to deal
#with any problems.