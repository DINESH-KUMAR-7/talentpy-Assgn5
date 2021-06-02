"""
Create a class Printer with a default constructor and a method called print_me(data), which
returns the data that comes as argument.

    Example: Let’s say obj is the object for Printer class.
        res = obj.print_me(“Welcome”)
        print(result)
        Output: Welcome
"""

class Printer:
    #Default Constructor - No arguments
    def __init__(self):
        pass

    #gets the data and returns it with modified String
    def print_me(self,data):
        data = "Output:"+" "+data
        return data

obj = Printer()
result = obj.print_me("Welcome")
print(result)

"""
Output:
/GitHub/talentpy-Assgn5/printer.py
Output: Welcome
"""