print("Sales initialised", __name__)


def calc_tax():
    pass


def calc_shipping():
    pass


if __name__ == "__main__":
    print("Sales started")
    calc_tax()

    
#Line 8-10 allows you to execute a module as a script but if you put this
#inside of a module inside of a module then you wont automaticly run this 
#script as the name of the file wont be __main__