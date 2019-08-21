"""
KLUCZOWE:
cls = type(self)
"""
class Person:
    age = 25

    def printAge(cls):
        print('The age is:', cls.age)
    
    def changeClassAtribute(self):
        print("ZMIANA atrbytubut klasy w metodzie")
        cls = type(self)
        cls.age = 999999999
        print(cls.age)
        

# create printAge class method
Person.printAge = classmethod(Person.printAge)

Person.printAge()
p = Person()
print(p.age)

print("Wywowalnie changeClassAtribute")
p.changeClassAtribute()
print(p.age)

print(Person.age)
Person.printAge()


# The age is: 25
# 25
# Wywowalnie changeClassAtribute
# ZMIANA atrbytubut klasy w metodzie
# 999999999
# 999999999
# 999999999
# The age is: 999999999