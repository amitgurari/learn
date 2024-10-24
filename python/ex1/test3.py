
def my_func(param1):
    print("my func: ",param1)

my_func("value")

class MyObject:
    def my_func(self, param1):
        print("myobject.myfunc: ", param1)


class Person:
    name: str
    age: int
    hair_color: str

    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
    
    def who_am_i(self):
        print("i am: ", self.name)
    
    def is_this_my_name(self, name):
        return self.name == name

person1 = Person("amit", 12, "blond")
person1.who_am_i()
print(person1.is_this_my_name("amit"))
print(person1.is_this_my_name("sahar"))

person2 = Person("sahar", 17, "black")
person2.who_am_i()
