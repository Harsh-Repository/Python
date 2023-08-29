def add_sub(x,y):
    add_result=x+y
    sub_result=x-y

    return add_result, sub_result
print (add_sub(100,77))

###########################

def positive_or_negative(num):
    if num>0:
        return "Positive"
    elif num<0:
        return "Negative"
    else:
        return "Zero"
    
print(positive_or_negative(100))
print(positive_or_negative(-13))
print(positive_or_negative(0))

#############################

def find_max_in_list(some_list):
    if len(some_list) == 0:
        # print("Zero element list!")
        return "Zero element list!"
    
    max_element = some_list[0]
    length= len(some_list)

    for i in range(1, length):
        if some_list[i] > max_element:
            max_element = some_list[i]

    return max_element

empty_list=[]
print(find_max_in_list(empty_list))

my_list=[12,12312,12432,143,134124,664563, 2141241243234]
print(find_max_in_list(my_list))

#############################

def find_first_capital_letter(some_string):
    capital_letter = None

    for ch in some_string:
        if ch.upper() == ch and ch!=" ":
            capital_letter=ch
            break
    
    if capital_letter is None:
        return "No capital letters found!"
    else:
        return "First capital letter " + capital_letter
    
print(find_first_capital_letter("how Are You?"))
print(find_first_capital_letter("hello world"))

##########################

def create_disctionary_representation(name, age, occupation):
    dictionary = {
        "name": name,
        "age": age,
        "occupation": occupation
    }
    return dictionary

info_dictionary = create_disctionary_representation("John", 35, "Engineer")
print (info_dictionary)
my_dictionary = create_disctionary_representation("Hasrhit", 25, "Full stack developer")
print(my_dictionary)

##############################
def generate_list(name, num_elements):
    return_list = []

    for i in range(num_elements):
        return_list.append(name)
    return return_list

test_list = generate_list("Hello", 4)
my_name = generate_list("Harshit",7)
print(test_list)
print(my_name)
###########################

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

x,y=10,5

print(add(x,y), sub(x,y), mul(x,y), div(x,y))

###########################

def calculate (a,b, operator):
    if operator == "addition":
        return a+b
    elif operator == "substract":
        return a-b
    elif operator == "multiply":
        return a*b
    elif operator == "division":
        return a/b
    else :
        return "Invalid operator!"

additionxy = calculate(100, 20, "addition")
substractxy = calculate(100, 20, "substract")
multiplyxy = calculate(100,20,"multiply")
divisionxy = calculate(100,20,"division")
nothingxy = calculate(100,20,"helloworld")

print (additionxy, substractxy, multiplyxy, divisionxy, nothingxy)

##########################