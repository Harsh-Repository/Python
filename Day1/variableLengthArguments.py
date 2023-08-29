def print_fn(string_1="\n"):
    print(string_1)

print_fn()
print_fn("Hello")
# print_fn("Hello", "World") ##TypeError: print_fn() takes from 0 to 1 positional arguments but 2 were given
###########################

def print_fn1(*args):
    args_type = type(args)
    print(args)

print_fn1()
print_fn1("Hello")
print_fn1("Hello", "World") ##No TypeError as *agrs will take any number of inputs
num_list = [3,6,1,5,4,2]
print_fn1(num_list)

############################

def students_in_college(college, city, *students):
    print("College: ", college)
    print("City: ", city)
    print("Students: ", students)

students_in_college("DSU","Bengaluru","Harshit","Abhinav","Yashu","Abhijith","Dheeraj","Sharan","Irol")