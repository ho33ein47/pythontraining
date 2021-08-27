''' this file will compare,
instance variables and class attribute(variables)
'''
class DaneshjooUo:
    'class without auto instance'
    pass

stu1 = DaneshjooUo()
stu1.fName = 'Arya'
stu1.lName = 'Aliyan'
stu1.age = 19

stu2 = DaneshjooUo()
stu2.fName = 'Mohammad'
stu2.lName = 'Osoolian'
stu2.age = 18

print(stu1.fName)
print(stu2.age)

# --

class DaneshjooAd:
    'this class with instance variable'
    def __init__(self, fName, lName, age):
        self.fName = fName
        self.lName = lName
        self.age = age

stu3 = DaneshjooAd('Shayan', 'Sarhadi', 19)
stu4 = DaneshjooAd('Amir', 'Tarsa', 19)

print(stu3.lName)
print(stu4.lName)