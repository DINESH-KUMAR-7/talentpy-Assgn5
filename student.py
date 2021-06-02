"""
Create a class Student with parameterised constructor name and gender. Create a getter which
returns name in the format Mr. <<name>> if the gender is Male, Ms. <<name>> if the gender is
Female.
"""
class Student:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    @property
    #getter method
    def _string(self):
        return self.name

    #setter method
    @_string.setter
    def _string(self,name):
        if self.gender == 'Male':
            self.name = "Mr."+name
        else:
            self.name = "Ms."+name

name_format = Student("Naruto","Male")
#giving the name for _string method to generate the string
name_format._string = "Naruto"
print(name_format._string)

"""
Output:
/GitHub/talentpy-Assgn5/student.py
Mr.Naruto
"""