
my_var = 7
print(my_var)
my_var = 12
print(my_var)

my_name = "amit"
print(my_name)
my_name = 'ran'
print(my_name)

print("-----------------")
mytext = "my text"
mytext = 'my text'
mytext="line1\nline2"
print(mytext)
print(len(mytext))
mytext="""line1
line2"""
print(mytext)
print("-----------------")

mynumbers="0123456789"
print(mynumbers)
some_numbers = mynumbers[0:]
print(some_numbers)
some_numbers = mynumbers[4:7]
print(some_numbers)
some_numbers = mynumbers[8:]
print(some_numbers)
some_numbers = mynumbers[-2:]
print(some_numbers)


print("--------------------")

def print_hello(first_name, last_name):
    print("start")
    print(f'not hello {first_name} {last_name}')
    print("end")

print_hello("ran", "gur ari")
print_hello("amit", "gur ari")

def return_bigger(num1, num2):
    if num1 > num2:
        return num1
    return num2

bigger = return_bigger(1, 2)
print(bigger)
bigger = return_bigger(2, 1)
print(bigger)
bigger = return_bigger(222, 123)
print(bigger)

print("--------------------")

value = 1
print(value)

def test123(value):
    print(value)

test123(2)
test123(3)
print(value)

print("--------------------")


def sum_3(a, b, c):
    sum = a + b + c
    print("sum:", sum)
    return sum

result = sum_3(10, 100, 1)
print(result)


def combine_text(text1,text2):
    return text1 + "-" + text2  

result = combine_text("gur", "ari")
print(result)

print("--------------------")

def test1(num1,num2):
    if num1*10>num2:
        return num1
    return num2

print(test1(1, 1))
print(test1(1, 5))
print(test1(1, 11))

print("--------------------")

def test2(num1,num2,num5):
    if num1 + num2 > num5:
        return num1 + num2
    return num5

print(test2(1 , 2,5))
print(test2(3, 3,5))

print("--------------------")

value = 1
print(value)
if True:
    value = 2
    print(value)
    if False:
        value = 3
        print(value)
print(value)


print("--------------------")

def my_func1(param1, param2):
    print("my func 1")
    print(param1)
    print(param2)

my_func1(1, 2)
my_func1("amit", "gur ari")
my_func1("hello", "world")
my_func1(66, "big number")

print("--------------------")

def my_func2(param1, param2, param3):
    print("my_func2 -> param1=", param1, "param2=", param2, "param3=", param3)

my_func2(1, 2, 3)
my_func2(1, param3=2, param2=3)

print("--------------------")

children = ["sahar", "ran", "amit"]
print(children)
boys = children[1:]
print(boys)
boys = children[-1:]
print(boys)

boys = ["ran", "amit"]
girls = ["sahar"]
children = boys + girls
print(children)
print(len(children))
children.clear()
print(children)
print(len(children))

print("--------------------")

mylist = ["a","a", 1, 1, 1, 3, 3, 3, 3, 3]
print(mylist)
print(len(mylist))
print(mylist[:2])

print("--------------------")

myset = {"a", "a", "a", 1, 1, 1}
print(myset)
print(len(myset))

print("--------------------")

my_dict = {"amit": 12, "sahar": 17}
print(my_dict)
print(len(my_dict))
print(my_dict["sahar"])
age = my_dict["sahar"]
print(age)


my_dict = {"amit": [12, "boy"], "sahar": [17, "girl"]}
values = my_dict["amit"]
print(values)