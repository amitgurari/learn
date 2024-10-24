
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
