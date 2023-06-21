high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student: 
    print("Eligible")
else:
    print("Not Eligible")
    
#The "and" function will only fire if both variables are True.
#The "or" function will fire if only one of the variables are True
#Using "()" around code means it is confinded to only whats inside
#the parenthesis like parenthesis in BIDMAS and only the result will 
#interact with the rest of the logical statement


#All logical operators are short circuit beause they operate like a circuit
#board and will not continue if a statement if False unless told otherwise.
#Look at line 26 if statement for context


# high_income = False
# good_credit = True
# student = False

# if high_income and good_credit and not student: 
#     print("Eligible")