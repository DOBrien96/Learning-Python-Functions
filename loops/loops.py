for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
    
#The range function can have up to 3 arguments, the first argument is what 
# you want the range to start from unless it's the only argument and then
#by default it will become the max number like argument 2. The last argument
#is the incrementation of the range, as you can see when you run the program
#it skips Attempt 2, Attempt 4 and so on.

succesful = True 
for number in range(3):
    print("Attempt")
    if succesful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
    
#Because successful is set to True line 13 will fire and break the loop
#but because the loop has a range of 3 (will run the loop 3 times and then stop)
#once the 3 attempts are up it will fire the else statement instead and end the loop

for x in range(5):
    for y in range(3):
        print(f"({x}. {y})")
        
#Lines 23 to 24 are called a nested loop because it is a loop inside a loop
#this is helpful when wanting to print out something like co-ordinates
#The way this works is x will fire and subtract 1 from the x range and then
#y will go through it's entire range before going back to the x range where
#x will subract only 1 once again y will be triggered to run the entire y
#range once more, until x has reached 0

command = ""
while command.lower() != "quit":
    command = input("> ")
    print("ECHO", command)
    
#while loop line 35 essentially is say "while command doesn't equal too quit
#keep running until the user types quit", the .lower() function makes sure
#everything typed is in lowercase so that no matter how someone writes the 
#word "QuIt" it will always be "quit" to meet the while loops requirments

command = ""
while True:
    command = input("> ")
    print("ECHO", command)
    if command.lower() == "quit":
        break

#The while loop from line 45 to 49 is the same as line 34 to 37 but 45 to 49
#is an infinite loop, this is helpfule because you don't have to define the
#command variable in the while line of the loop, be careful though as you
#will need to ensure the loop breaks at some point otherwise it will go on
#forever and crash your program.